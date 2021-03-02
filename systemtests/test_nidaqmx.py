import pytest
import nidaqmx
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.mark.sequence_file("nidaqmx.seq")
def test_nidaqmx(system_test_runner):
    assert system_test_runner.run()


@nitsm.codemoduleapi.code_module
def create_tasks(tsm_context: SemiconductorModuleContext):
    task_names, channel_lists = tsm_context.get_all_nidaqmx_task_names("")
    tasks = [nidaqmx.Task(task_name) for task_name in task_names]

    for task_name, task, channel_list in zip(task_names, tasks, channel_lists):
        tsm_context.set_nidaqmx_task(task_name, task)
        channel_list = nidaqmx.utils.unflatten_channel_string(channel_list)
        for channel in channel_list:
            task.ai_channels.add_ai_voltage_chan(
                task.name + "/ai" + channel, min_val=4.9, max_val=5.1
            )


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
):
    (
        pin_query,
        queried_tasks,
        _,
    ) = tsm_context.pins_to_nidaqmx_tasks(pins)
    expected_instrument_names = set(expected_instrument_names)
    valid_instruments = []

    for task in queried_tasks:
        # call some methods on the task to ensure no errors
        task.read()

        # check instrument name we received is in the set of instrument names we expected
        for device in task.devices:
            actual_instrument_name = device.name
            valid_instruments.append(actual_instrument_name in expected_instrument_names)
            expected_instrument_names -= {actual_instrument_name}

    pin_query.publish(valid_instruments)
    num_missing_instruments = [len(expected_instrument_names)] * len(queried_tasks)
    pin_query.publish(num_missing_instruments, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_tasks(tsm_context: SemiconductorModuleContext):
    queried_tasks = tsm_context.get_all_nidaqmx_tasks("")
    for task in queried_tasks:
        task.close()
