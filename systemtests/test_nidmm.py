import pytest
import nidmm
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext

OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "4071", "BoardType": "PXI"}}


@pytest.mark.sequence_file("nidmm.seq")
def test_nidmm(system_test_runner):
    assert system_test_runner.run()


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_nidmm_instrument_names()
    for instrument_name in instrument_names:
        session = nidmm.Session(instrument_name, options=OPTIONS)
        tsm_context.set_nidmm_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
):
    pin_query, sessions = tsm_context.pins_to_nidmm_sessions(pins)
    expected_instrument_names = set(expected_instrument_names)
    valid_instruments = []

    for session in sessions:
        # call some methods on the session to ensure no errors
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        session.read()
        session.abort()

        # check instrument name we received is in the set of instrument names we expected
        actual_instrument_name = session.io_resource_descriptor
        valid_instruments.append(actual_instrument_name in expected_instrument_names)
        expected_instrument_names -= {actual_instrument_name}

    pin_query.publish(valid_instruments)
    num_missing_instruments = [len(expected_instrument_names)] * len(sessions)
    pin_query.publish(num_missing_instruments, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidmm_sessions()
    for session in sessions:
        session.close()
