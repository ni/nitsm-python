import os
import os.path
import sys
import shutil
import subprocess
import winreg
import pytest

_python_version = ".".join(map(str, sys.version_info[:2]))
try:
    _python_environment_path = os.environ["VIRTUAL_ENV"]
except KeyError:
    _python_environment_path = ""  # global interpreter

def get_env_variable_from_registry(variable_name):
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Control\Session Manager\Environment")
    return winreg.QueryValueEx(key, variable_name)[0]

_teststand_public_path = get_env_variable_from_registry("TestStandPublic64")

class SystemTestRunner:
    # subprocess.run with check=True will throw an exception if the return code is non-zero
    # with stdout set to subprocess.PIPE, exit code and stdout will be included in the exception
    _SUBPROCESS_RUN_OPTIONS = {"stdout": subprocess.PIPE, "timeout": 180, "check": True}

    # we need to get the TestStand variables from the registry since the pipeline process 
    # does not refresh its environment after running the TestStand version selector

    _csharp_oi_path = os.path.join(
        _teststand_public_path,
        "UserInterfaces",
        "Simple",
        "CSharp",
        "Source Code",
        "bin",
        "x64",
        "release",
        "TestExec.exe",
    )

    _test_fixture_path = os.path.join(os.path.dirname(__file__), "SystemTestFixture.seq")

    _offline_mode_tool_path = os.path.join(
        os.environ["ProgramFiles(x86)"],
        "National Instruments",
        "Shared",
        "OfflineMode",
        "NationalInstruments.Semiconductor.OfflineModeAPITool.exe",
    )

    def __init__(self, sequence_file_path, offline_mode_cfg_path=""):
        self._sequence_file_path = sequence_file_path
        self._offline_mode_cfg_path = offline_mode_cfg_path

    def __enter__(self):
        if self._offline_mode_cfg_path:
            subprocess.run(
                [self._offline_mode_tool_path, "/enter", self._offline_mode_cfg_path],
                **self._SUBPROCESS_RUN_OPTIONS,
            )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._offline_mode_cfg_path:
            subprocess.run([self._offline_mode_tool_path, "/leave"], **self._SUBPROCESS_RUN_OPTIONS)

    def run(self):
        subprocess.run(
            [
                self._csharp_oi_path,
                "/outputtostdio",
                "/run",
                "MainSequence",
                self._test_fixture_path,
                "/pyrunentrypoint",
                "Test UUTs",
                self._sequence_file_path,
                "/pyversion",
                _python_version,
                "/pyenvironment",
                _python_environment_path,
                "/quit",
            ],
            **self._SUBPROCESS_RUN_OPTIONS,
        )
        return True

@pytest.fixture(scope="session", autouse=True)
def teststand_login_override():
    system_tests_front_end_callbacks_path = os.path.join(
        os.path.dirname(__file__), "FrontEndCallbacks.seq"
    )
    teststand_front_end_callbacks_path = os.path.join(
        _teststand_public_path, "Components", "Callbacks", "FrontEnd", "FrontEndCallbacks.seq"
    )
    teststand_backup_front_end_callbacks_path = os.path.join(
        _teststand_public_path, "Components", "Callbacks", "FrontEnd", "FrontEndCallbacks.seq.bak"
    )
    os.replace(teststand_front_end_callbacks_path, teststand_backup_front_end_callbacks_path)
    shutil.copy(system_tests_front_end_callbacks_path, teststand_front_end_callbacks_path)
    yield None
    os.replace(teststand_backup_front_end_callbacks_path, teststand_front_end_callbacks_path)


@pytest.fixture
def system_test_runner(request):
    # get absolute path of the test program file which is assumed to be relative to the test module
    module_directory = os.path.dirname(request.module.__file__)

    sequence_file_name = request.node.get_closest_marker("sequence_file").args[0]
    sequence_file_path = os.path.join(module_directory, sequence_file_name)

    offline_mode_marker = request.node.get_closest_marker("offline_mode")
    if offline_mode_marker:
        offline_mode_cfg_name = offline_mode_marker.args[0]
        offline_mode_cfg_path = os.path.join(module_directory, offline_mode_cfg_name)
    else:
        offline_mode_cfg_path = ""

    with SystemTestRunner(sequence_file_path, offline_mode_cfg_path) as test_runner:
        # the context manager will enter and exit offline mode if the marker was supplied
        yield test_runner
