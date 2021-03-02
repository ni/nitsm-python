import pytest
import nifgen
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.mark.sequence_file("nifgen.seq")
def test_nifgen(system_test_runner):
    assert system_test_runner.run()


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_nifgen_instrument_names()
    for instrument_name in instrument_names:
        # Cannot set simulated session with instrument name
        session = nifgen.Session("", options={"Simulate": True})
        tsm_context.set_nifgen_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
    expected_channel_lists,
):
    pin_query, sessions, channel_lists = tsm_context.pins_to_nifgen_sessions(pins)
    expected_instrument_channels = set(zip(expected_instrument_names, expected_channel_lists))
    valid_channels = []

    for session, channel_list in zip(sessions, channel_lists):
        # call some methods on the session to ensure no errors
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(nifgen.Waveform.DC, 0, 0, 1)
        session.initiate()
        session.abort()

        # check instrument channel we received is in the set of instrument channels we expected
        actual_instrument_channel = (session.io_resource_descriptor, channel_list)
        valid_channels.append(actual_instrument_channel in expected_instrument_channels)
        expected_instrument_channels -= {actual_instrument_channel}

    pin_query.publish(valid_channels)
    num_missing_channels = [len(expected_instrument_channels)] * len(sessions)
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nifgen_sessions()
    for session in sessions:
        session.close()
