import pytest
import subprocess
import os
import shutil
import stat

from subprocess import check_output


class TestSystem:

    def test_system(self):
        module_directory = os.path.dirname(__file__)
        sequence_file_path = os.path.join(module_directory, "..", "systemtests", "nidcpower_legacy.seq")

        self._setup_front_end_callbacks()

        teststand_path = os.environ["TestStand64"]
        csharp_oi_path = os.path.join(teststand_path, "UserInterfaces", "Simple", "CSharp", "Source Code", "bin", "x64",
                                      "release", "TestExec.exe")

        arguments = "/runentrypoint \"Test UUTs\" " + sequence_file_path + " /quit"
        command_line = csharp_oi_path + " " + arguments

        completed_process = subprocess.run(command_line)
        assert completed_process.returncode == 0

        self._cleanup_front_end_callbacks()

    def _setup_front_end_callbacks(self):
        teststand_public_path = os.environ["TestStandPublic64"]
        src_front_end_callbacks_path = os.path.join(os.path.dirname(__file__), "FrontEndCallbacks.seq")
        dst_front_end_callbacks_path = os.path.join(teststand_public_path, "Components", "Callbacks", "FrontEnd",
                                                    "FrontEndCallbacks.seq")
        backup_front_end_callbacks_path = os.path.join(teststand_public_path, "Components", "Callbacks", "FrontEnd",
                                                       "FrontEndCallbacks.seq.bak")
        os.chmod(dst_front_end_callbacks_path, stat.S_IWRITE)
        os.chmod(backup_front_end_callbacks_path, stat.S_IWRITE)
        os.replace(dst_front_end_callbacks_path, backup_front_end_callbacks_path)
        shutil.copy(src_front_end_callbacks_path, dst_front_end_callbacks_path)

    def _cleanup_front_end_callbacks(self):
        teststand_public_path = os.environ["TestStandPublic64"]
        dst_front_end_callbacks_path = os.path.join(teststand_public_path, "Components", "Callbacks", "FrontEnd",
                                                    "FrontEndCallbacks.seq")
        backup_front_end_callbacks_path = os.path.join(teststand_public_path, "Components", "Callbacks", "FrontEnd",
                                                       "FrontEndCallbacks.seq.bak")
        os.chmod(dst_front_end_callbacks_path, stat.S_IWRITE)
        os.replace(backup_front_end_callbacks_path, dst_front_end_callbacks_path)
