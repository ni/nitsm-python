import pytest


@pytest.mark.skip("Not yet implemented.")
@pytest.mark.sequence_file("nidmm.seq")
def test_nidmm(system_test_runner):
    system_test_runner.run()
