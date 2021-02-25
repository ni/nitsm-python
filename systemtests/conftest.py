import os
import os.path
import shutil
import subprocess
import pytest

_teststand_public_path = os.environ["TestStandPublic64"]


class SystemTestRunner:
    def __init__(self, sequence_file_path):
        self._sequence_file_path = sequence_file_path

    def run(self):
        csharp_oi_path = os.path.join(
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
        # subprocess.run with check=True will throw an exception if the return code is non-zero
        # with stdout set to subprocess.PIPE, exit code and stdout will be included in the exception
        subprocess.run(
            [
                csharp_oi_path,
                "/outputtostdio",
                "/runentrypoint",
                "Test UUTs",
                self._sequence_file_path,
                "/quit",
            ],
            stdout=subprocess.PIPE,
            timeout=60,
            check=True,
        )
        return True


@pytest.fixture(scope="session")
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
def system_test_runner(request, teststand_login_override):
    # get absolute path of the test program file which is assumed to be relative to the test module
    sequence_file_name = request.node.get_closest_marker("sequence_file").args[0]
    module_directory = os.path.dirname(request.module.__file__)
    sequence_file_path = os.path.join(module_directory, sequence_file_name)
    return SystemTestRunner(sequence_file_path)
