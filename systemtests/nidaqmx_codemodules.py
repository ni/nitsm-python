import nidaqmx
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext
from sessionutils import get_task_name_from_task


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    # get task names and channel lists
    ai_task_names, ai_channel_lists = tsm_context.get_all_nidaqmx_task_names("ai")
    ao_task_names, ao_channel_lists = tsm_context.get_all_nidaqmx_task_names("ao")

    # create and set ai tasks
    for task_name, channel_list in zip(ai_task_names, ai_channel_lists):
        task = nidaqmx.Task(task_name)
        task.ai_channels.add_ai_voltage_chan(channel_list)
        tsm_context.set_nidaqmx_task(task_name, task)

    # create and set ao tasks
    for task_name, channel_list in zip(ao_task_names, ao_channel_lists):
        task = nidaqmx.Task(task_name)
        task.ao_channels.add_ao_voltage_chan(channel_list)
        tsm_context.set_nidaqmx_task(task_name, task)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_task_names,
    expected_channel_lists,
):
    pin_query, tasks, channel_lists = tsm_context.pins_to_nidaqmx_tasks(pins)
    expected_instrument_channels = set(zip(expected_task_names, expected_channel_lists))
    valid_channels = []

    for task, channel_list in zip(tasks, channel_lists):
        # call some methods on the session to ensure no errors
        task.timing.cfg_samp_clk_timing(1e3, "OnboardClock", samps_per_chan=10)
        task.start()
        task.read(-1)
        task.stop()

        # check instrument channel we received is in the set of instrument channels we expected
        task_name = get_task_name_from_task(task)
        actual_instrument_channel = (task_name, channel_list)
        valid_channel = actual_instrument_channel in expected_instrument_channels
        valid_channels.append([valid_channel] * len(channel_list.split(", ")))
        expected_instrument_channels -= {actual_instrument_channel}

    pin_query.publish(valid_channels)
    num_missing_channels = [
        [len(expected_instrument_channels)] * len(row) for row in valid_channels
    ]
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    tasks = tsm_context.get_all_nidaqmx_tasks("")
    for task in tasks:
        task.close()
