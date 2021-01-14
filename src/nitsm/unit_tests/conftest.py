import os.path
import pytest
import win32com.client
import win32com.client.selecttlb
import pythoncom
import nitsm.codemoduleapi


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


class PublishedData:
    def __init__(self, published_data_com_obj):
        published_data_com_obj._oleobj_ = published_data_com_obj._oleobj_.QueryInterface(
            published_data_com_obj.CLSID, pythoncom.IID_IDispatch
        )
        self._published_data = published_data_com_obj

    @property
    def boolean_value(self):
        return self._published_data.BooleanValue

    @property
    def double_value(self):
        return self._published_data.DoubleValue

    @property
    def pin(self):
        return self._published_data.Pin

    @property
    def published_data_id(self):
        return self._published_data.PublishedDataId

    @property
    def site_number(self):
        return self._published_data.SiteNumber

    @property
    def string_value(self):
        return self._published_data.StringValue

    @property
    def type(self):
        return self._published_data.Type


class PublishedDataReader:
    _tlb = win32com.client.selecttlb.FindTlbsWithDescription(
        "NI TestStand Semiconductor Module Standalone Semiconductor Module Context"
    )[0]

    def __init__(self, published_data_reader_com_obj):
        self._published_data_reader = win32com.client.CastTo(
            published_data_reader_com_obj, "IPublishedDataReader", self._tlb
        )

    def get_and_clear_published_data(self):
        published_data = self._published_data_reader.GetAndClearPublishedData()
        for published_data_point in published_data:
            published_data_point = win32com.client.CastTo(
                published_data_point, "IPublishedData", self._tlb
            )
            yield PublishedData(published_data_point)


@pytest.fixture
def published_data_reader(_published_data_reader_factory):
    return PublishedDataReader(_published_data_reader_factory[1])
