import pytest

from tests.conftest import SystemTestRunner


class TestSystem:

    @pytest.mark.sequence_file("nidcpower_legacy.seq")
    def test_nidcpower_legacy(self, test_sequence_file_path):
        SystemTestRunner.run_system_test(test_sequence_file_path)

    # Can't enable this test until nidcpower python supports channel expansion
    # @pytest.mark.sequence_file("nidcpower.seq")
    # def test_nidcpower(self, test_sequence_file_path):
    #    SystemTestRunner.run_system_test(test_sequence_file_path)

    # not yet implemented
    @pytest.mark.sequence_file("nidmm.seq")
    def test_nidmm(self, test_sequence_file_path):
        SystemTestRunner.run_system_test(test_sequence_file_path)
