import nidaqmx
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import NIDAQmxSinglePinSingleTaskQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIDAQmxSinglePinMultipleTaskQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIDAQmxMultiplePinSingleTaskQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIDAQmxMultiplePinMultipleTaskQueryContext


@pytest.fixture
def simulated_nidaqmx_tasks1(standalone_tsm_context):
    task_names, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("ai")
    tasks = [nidaqmx.Task(tsk_name) for tsk_name in task_names]
    for task_name, task in zip(task_names, tasks):
        standalone_tsm_context.set_nidaqmx_task(task_name, task)
    yield tasks
    for task in tasks:
        task.close()


@pytest.fixture
def simulated_nidaqmx_tasks2(standalone_tsm_context):
    task_names, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("ao")
    tasks = [nidaqmx.Task(tsk_name) for tsk_name in task_names]
    for task_name, task in zip(task_names, tasks):
        standalone_tsm_context.set_nidaqmx_task(task_name, task)
    yield tasks
    for task in tasks:
        task.close()


@pytest.fixture
def simulated_nidaqmx_tasks(standalone_tsm_context):
    task_names1, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("ai")
    task_names2, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("ao")
    tasks = [nidaqmx.Task(tsk_name) for tsk_name in task_names1 + task_names2]
    for task_name, task in zip(task_names1 + task_names2, tasks):
        standalone_tsm_context.set_nidaqmx_task(task_name, task)
    yield tasks
    for task in tasks:
        task.close()


@pytest.mark.pin_map("nidaqmx.pinmap")
class TestNIDAQmx:
    pin_map_instruments = ["DAQmx1", "DAQmx2", "DAQmx3"]
    pin_map_task_types = ["ai", "ao"]
    pin_map_dut_pins1 = ["DUTPin1"]
    pin_map_dut_pins2 = ["DUTPin2"]
    pin_map_system_pins1 = ["SystemPin1"]
    pin_map_system_pins2 = ["SystemPin2"]
    pin_map_pin_groups = ["PinGroup1"]

    def test_get_all_nidaqmx_task_names(self, standalone_tsm_context: SemiconductorModuleContext):
        for task_type in self.pin_map_task_types:
            (
                task_names,
                channel_lists,
            ) = standalone_tsm_context.get_all_nidaqmx_task_names(task_type)
            assert isinstance(task_names, tuple)
            assert isinstance(channel_lists, tuple)
            assert len(task_names) == len(channel_lists)
            for task_name, channel_list in zip(task_names, channel_lists):
                assert isinstance(task_name, str)
                assert isinstance(channel_list, str)
                assert task_name in self.pin_map_instruments

    def test_set_nidaqmx_task(self, standalone_tsm_context: SemiconductorModuleContext):
        for task_type in self.pin_map_task_types:
            (
                task_names,
                channel_lists,
            ) = standalone_tsm_context.get_all_nidaqmx_task_names(task_type)
            for task_name, channel_list in zip(task_names, channel_lists):
                with nidaqmx.Task(task_name) as task:
                    standalone_tsm_context.set_nidaqmx_task(task_name, task)
                    assert SemiconductorModuleContext._sessions[id(task)] is task

    def test_get_all_nidaqmx_tasks1(self, standalone_tsm_context, simulated_nidaqmx_tasks1):
        queried_tasks = standalone_tsm_context.get_all_nidaqmx_tasks("ai")
        for queried_task in queried_tasks:
            assert isinstance(queried_task, nidaqmx.Task)
            assert queried_task in simulated_nidaqmx_tasks1
        assert len(queried_tasks) == len(simulated_nidaqmx_tasks1)

    def test_get_all_nidaqmx_tasks2(self, standalone_tsm_context, simulated_nidaqmx_tasks2):
        queried_tasks = standalone_tsm_context.get_all_nidaqmx_tasks("ao")
        for queried_task in queried_tasks:
            assert isinstance(queried_task, nidaqmx.Task)
            assert queried_task in simulated_nidaqmx_tasks2
        assert len(queried_tasks) == len(simulated_nidaqmx_tasks2)

    def test_pin_to_nidaqmx_task(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        for system_pin in self.pin_map_system_pins1:
            (
                pin_query_context,
                queried_task,
                queried_channel_list,
            ) = standalone_tsm_context.pin_to_nidaqmx_task(system_pin)
            assert isinstance(pin_query_context, NIDAQmxSinglePinSingleTaskQueryContext)
            assert isinstance(queried_task, nidaqmx.Task)
            assert isinstance(queried_channel_list, str)
            assert queried_task in simulated_nidaqmx_tasks

    def test_pin_to_nidaqmx_tasks(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        for pin_group in self.pin_map_pin_groups:
            (
                pin_query_context,
                queried_tasks,
                queried_channel_lists,
            ) = standalone_tsm_context.pin_to_nidaqmx_tasks(pin_group)
            assert isinstance(pin_query_context, NIDAQmxSinglePinMultipleTaskQueryContext)
            assert isinstance(queried_channel_lists, tuple)
            assert len(queried_tasks) == len(queried_channel_lists)
            for queried_task in queried_tasks:
                assert isinstance(queried_task, nidaqmx.Task)
                assert queried_task in simulated_nidaqmx_tasks

    def test_pins_to_nidaqmx_task(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        all_pins = self.pin_map_dut_pins1 + self.pin_map_system_pins1
        (
            pin_query_context,
            queried_task,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nidaqmx_task(all_pins)
        assert isinstance(pin_query_context, NIDAQmxMultiplePinSingleTaskQueryContext)
        assert isinstance(queried_task, nidaqmx.Task)
        assert isinstance(queried_channel_list, str)
        assert queried_task in simulated_nidaqmx_tasks

    def test_pins_to_nidaqmx_tasks(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        all_pins = self.pin_map_dut_pins2 + self.pin_map_system_pins2
        (
            pin_query_context,
            queried_tasks,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nidaqmx_tasks(all_pins)
        assert isinstance(pin_query_context, NIDAQmxMultiplePinMultipleTaskQueryContext)
        assert isinstance(queried_tasks, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_tasks) == len(queried_channel_lists)
        for queried_task in queried_tasks:
            assert isinstance(queried_task, nidaqmx.Task)
            assert queried_task in simulated_nidaqmx_tasks
