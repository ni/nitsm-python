import os.path
import pytest
import win32com.client
import win32com.client.selecttlb
import pythoncom
import nitsm.codemoduleapi
import os
import shutil
import stat
import subprocess


_standalone_tsm_context_tlb = win32com.client.selecttlb.FindTlbsWithDescription(
    "NI TestStand Semiconductor Module Standalone Semiconductor Module Context"
)[0]

@pytest.fixture
def test_sequence_file_path(request):
    # get absolute path of the test program file which is assumed to be relative to the test module
    sequence_file_name = request.node.get_closest_marker("sequence_file").args[0]
    module_directory = os.path.dirname(request.module.__file__)
    # temporary path until we decide on best location for sequence files.
    sequence_file_path = os.path.join(module_directory, "..", "systemtests", sequence_file_name)
    return sequence_file_path

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
        self._published_data = win32com.client.CastTo(
            published_data_com_obj, "IPublishedData", _standalone_tsm_context_tlb
        )
        self._published_data._oleobj_ = self._published_data._oleobj_.QueryInterface(
            self._published_data.CLSID, pythoncom.IID_IDispatch
        )

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
    def __init__(self, published_data_reader_com_obj):
        self._published_data_reader = win32com.client.CastTo(
            published_data_reader_com_obj, "IPublishedDataReader", _standalone_tsm_context_tlb
        )

    def get_and_clear_published_data(self):
        published_data = self._published_data_reader.GetAndClearPublishedData()
        return [PublishedData(published_data_point) for published_data_point in published_data]


@pytest.fixture
def published_data_reader(_published_data_reader_factory):
    return PublishedDataReader(_published_data_reader_factory[1])


class SystemTestRunner:
    @staticmethod
    def run_system_test(sequence_file_path):
        teststand_path = os.environ["TestStand64"]
        csharp_oi_path = os.path.join(teststand_path, "UserInterfaces", "Simple", "CSharp", "Source Code", "bin", "x64",
                                  "release", "TestExec.exe")

        arguments = "/runentrypoint \"Test UUTs\" " + sequence_file_path + " /quit"
        command_line = csharp_oi_path + " " + arguments

        SystemTestRunner._setup_front_end_callbacks()
        completed_process = subprocess.run(command_line, timeout=60)
        SystemTestRunner._cleanup_front_end_callbacks()

        assert completed_process.returncode == 0

    # Replacing TestStand FrontEndCallbacks.seq prevents TestStand from displaying the login dialog on launch
    @staticmethod
    def _setup_front_end_callbacks():
        teststand_public_path = os.environ["TestStandPublic64"]
        src_front_end_callbacks_path = os.path.join(os.path.dirname(__file__), "FrontEndCallbacks.seq")
        dst_front_end_callbacks_path = os.path.join(teststand_public_path, "Components", "Callbacks", "FrontEnd",
                                                    "FrontEndCallbacks.seq")
        backup_front_end_callbacks_path = os.path.join(teststand_public_path, "Components", "Callbacks", "FrontEnd",
                                                       "FrontEndCallbacks.seq.bak")
        if os.path.exists(dst_front_end_callbacks_path):
            os.chmod(dst_front_end_callbacks_path, stat.S_IWRITE)
        if os.path.exists(backup_front_end_callbacks_path):
            os.chmod(backup_front_end_callbacks_path, stat.S_IWRITE)
        os.replace(dst_front_end_callbacks_path, backup_front_end_callbacks_path)
        shutil.copy(src_front_end_callbacks_path, dst_front_end_callbacks_path)

    @staticmethod
    def _cleanup_front_end_callbacks():
        teststand_public_path = os.environ["TestStandPublic64"]
        dst_front_end_callbacks_path = os.path.join(teststand_public_path, "Components", "Callbacks", "FrontEnd",
                                                    "FrontEndCallbacks.seq")
        backup_front_end_callbacks_path = os.path.join(teststand_public_path, "Components", "Callbacks", "FrontEnd",
                                                       "FrontEndCallbacks.seq.bak")
        os.chmod(dst_front_end_callbacks_path, stat.S_IWRITE)
        os.replace(backup_front_end_callbacks_path, dst_front_end_callbacks_path)