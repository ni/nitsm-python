import pytest


@pytest.mark.sequence_file("nidmm.seq")
def test_nidmm(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nidcpower.seq")
def test_nidcpower(system_test_runner):
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


@pytest.mark.sequence_file("nirelaydriver.seq")
def test_nirelaydriver(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("custom_instruments.seq")
def test_custom_instruments(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("site_and_global_data.seq")
def test_site_and_global_data(system_test_runner):
    assert system_test_runner.run()
