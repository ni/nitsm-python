import nidaqmx
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.pinquerycontexts import NIDAQmxSinglePinSingleTaskQueryContext
from nitsm.pinquerycontexts import NIDAQmxSinglePinMultipleTaskQueryContext
from nitsm.pinquerycontexts import NIDAQmxMultiplePinSingleTaskQueryContext
from nitsm.pinquerycontexts import NIDAQmxMultiplePinMultipleTaskQueryContext


@pytest.fixture
def simulated_nidaqmx_tasks(standalone_tsm_context):
    task_names, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("")
    tasks = [nidaqmx.Task(tsk_name) for tsk_name in task_names]
    for task_name, task in zip(task_names, tasks):
        standalone_tsm_context.set_nidaqmx_task(task_name, task)
    yield tasks
    for task in tasks:
        task.close()


@pytest.mark.pin_map("nidaqmx.pinmap")
class TestNIDAQmx:
    pin_map_instruments = ["DAQmx1", "DAQmx2"]
    pin_map_dut_pins = ["DUTPin1", "DUTPin2"]
    pin_map_system_pins = ["SystemPin1"]

    def test_get_all_nidaqmx_task_names(self, standalone_tsm_context: SemiconductorModuleContext):
        task_names, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("")
        assert isinstance(task_names, tuple)
        assert isinstance(channel_lists, tuple)
        assert len(task_names) == len(channel_lists)
        for task_name, channel_list in zip(task_names, channel_lists):
            assert isinstance(task_name, str)
            assert isinstance(channel_list, str)
            assert task_name in self.pin_map_instruments

    def test_set_nidaqmx_task(self, standalone_tsm_context: SemiconductorModuleContext):
        task_names, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("")
        for task_name, channel_list in zip(task_names, channel_lists):
            with nidaqmx.Task(task_name) as task:
                standalone_tsm_context.set_nidaqmx_task(task_name, task)
                assert SemiconductorModuleContext._sessions[id(task)] is task

    def test_get_all_nidaqmx_tasks(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        queried_tasks = standalone_tsm_context.get_all_nidaqmx_tasks("")
        assert isinstance(queried_tasks, tuple)
        assert len(queried_tasks) == len(simulated_nidaqmx_tasks)
        for queried_task in queried_tasks:
            assert isinstance(queried_task, nidaqmx.Task)
            assert queried_task in simulated_nidaqmx_tasks

    def test_pin_to_nidaqmx_task(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        (
            pin_query_context,
            queried_task,
            queried_channel_list,
        ) = standalone_tsm_context.pin_to_nidaqmx_task("SystemPin1")
        assert isinstance(pin_query_context, NIDAQmxSinglePinSingleTaskQueryContext)
        assert isinstance(queried_task, nidaqmx.Task)
        assert isinstance(queried_channel_list, str)
        assert queried_task in simulated_nidaqmx_tasks

    def test_pin_to_nidaqmx_tasks(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        (
            pin_query_context,
            queried_tasks,
            queried_channel_lists,
        ) = standalone_tsm_context.pin_to_nidaqmx_tasks("PinGroup1")
        assert isinstance(pin_query_context, NIDAQmxSinglePinMultipleTaskQueryContext)
        assert isinstance(queried_tasks, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_tasks) == len(queried_channel_lists)
        for queried_task, queried_channel_list in zip(queried_tasks, queried_channel_lists):
            assert isinstance(queried_task, nidaqmx.Task)
            assert isinstance(queried_channel_list, str)
            assert queried_task in simulated_nidaqmx_tasks

    def test_pins_to_nidaqmx_task(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        (
            pin_query_context,
            queried_task,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nidaqmx_task(self.pin_map_dut_pins)
        assert isinstance(pin_query_context, NIDAQmxMultiplePinSingleTaskQueryContext)
        assert isinstance(queried_task, nidaqmx.Task)
        assert isinstance(queried_channel_list, str)
        assert queried_task in simulated_nidaqmx_tasks

    def test_pins_to_nidaqmx_tasks(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_tasks,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nidaqmx_tasks(all_pins)
        assert isinstance(pin_query_context, NIDAQmxMultiplePinMultipleTaskQueryContext)
        assert isinstance(queried_tasks, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_tasks) == len(queried_channel_lists)
        for queried_task, queried_channel_list in zip(queried_tasks, queried_channel_lists):
            assert isinstance(queried_task, nidaqmx.Task)
            assert isinstance(queried_channel_list, str)
            assert queried_task in simulated_nidaqmx_tasks
