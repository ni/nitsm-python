import subprocess
import os
import shutil
import stat
import pytest

from tests.conftest import SystemTestRunner


@pytest.mark.sequence_file("nidcpower_legacy.seq")
class TestNIDCPowerSystem:

    def test_nidcpower_system(self, test_sequence_file_path):
        SystemTestRunner.run_system_test(test_sequence_file_path)


