import os.path
import pytest
import win32com.client
import win32com.client.selecttlb
import nitsm.codemoduleapi


def _find_standalone_tsm_context_tlb():
    tlbs = win32com.client.selecttlb.FindTlbsWithDescription(
        "NI TestStand Semiconductor Module Standalone Semiconductor Module Context"
    )
    return tlbs[0]


standalone_tsm_context_tlb = _find_standalone_tsm_context_tlb()


@pytest.fixture
def _published_data_reader_factory(request):
    # get absolute path of the pin map file which is assumed to be relative to the test module
    pin_map_path = request.node.get_closest_marker("pin_map").args[0]
    module_directory = os.path.dirname(request.module.__file__)
    pin_map_path = os.path.join(module_directory, pin_map_path)

    published_data_reader_factory = win32com.client.Dispatch(
        "NationalInstruments.TestStand.SemiconductorModule.Restricted.PublishedDataReaderFactory"
    )
    return published_data_reader_factory.NewSemiconductorModuleContext(pin_map_path)


@pytest.fixture
def standalone_tsm_context(_published_data_reader_factory):
    return nitsm.codemoduleapi.SemiconductorModuleContext(_published_data_reader_factory[0])


@pytest.fixture
def published_data_reader(_published_data_reader_factory):
    published_data_reader = win32com.client.CastTo(
        _published_data_reader_factory[1], "IPublishedDataReader", standalone_tsm_context_tlb
    )
    return published_data_reader
