import pytest
import win32com.client
import win32com.client.selecttlb
import nitsm.codemoduleapi


@pytest.fixture
def _published_data_reader_factory(request):
    pin_map_path = request.node.get_closest_marker('pin_map').args[0]
    published_data_reader_factory = win32com.client.Dispatch(
        "NationalInstruments.TestStand.SemiconductorModule.Restricted.PublishedDataReaderFactory"
    )
    return published_data_reader_factory.NewSemiconductorModuleContext(pin_map_path)


@pytest.fixture
def standalone_tsm_context(_published_data_reader_factory):
    return nitsm.codemoduleapi.SemiconductorModuleContext(_published_data_reader_factory[0])


@pytest.fixture
def published_data_reader(_published_data_reader_factory):
    typelibs = win32com.client.selecttlb.FindTlbsWithDescription(
        "NI TestStand Semiconductor Module Standalone Semiconductor Module Context"
    )
    standalone_tsm_typelib = typelibs[0]

    published_data_reader = win32com.client.CastTo(
        _published_data_reader_factory[1], "IPublishedDataReader", standalone_tsm_typelib
    )
    return published_data_reader
