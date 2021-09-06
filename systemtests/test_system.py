import pytest


@pytest.mark.sequence_file("nidmm.seq")
def test_nidmm(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.skip("Can't enable this test until nidcpower python supports channel expansion.")
@pytest.mark.sequence_file("nidcpower.seq")
def test_nidcpower(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nidcpower_legacy.seq")
def test_nidcpower_legacy(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nifgen.seq")
def test_nifgen(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nidaqmx.seq")
@pytest.mark.offline_mode("nidaqmx.offlinecfg")
def test_nidaqmx(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("niscope.seq")
def test_niscope(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nidigital.seq")
def test_nidigital(system_test_runner):
    assert system_test_runner.run()
