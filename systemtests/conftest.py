import os.path
import shutil
import stat
import subprocess

import pytest


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


@pytest.fixture
def test_sequence_file_path(request):
    # get absolute path of the test program file which is assumed to be relative to the test module
    sequence_file_name = request.node.get_closest_marker("sequence_file").args[0]
    module_directory = os.path.dirname(request.module.__file__)
    # temporary path until we decide on best location for sequence files.
    sequence_file_path = os.path.join(module_directory, "..", "systemtests", sequence_file_name)
    return sequence_file_path