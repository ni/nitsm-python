import re
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
        name, model = instrument_name.split("_")
        session = nifgen.Session(name, options={"Simulate": True, "DriverSetup": {"Model": model}})
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
        session.channels[channel_list].configure_standard_waveform(nifgen.Waveform.DC, 0, 0, 1)
        session.channels[channel_list].output_enabled = True
        session.initiate()
        session.abort()

        # check instrument channel we received is in the set of instrument channels we expected
        resource_name = re.search(r"resource_name='(\w*)'", repr(session)).group(1)
        actual_instrument_channel = (resource_name, channel_list)
        valid_channel = actual_instrument_channel in expected_instrument_channels
        valid_channels.append([valid_channel] * len(channel_list.split(", ")))
        expected_instrument_channels -= {actual_instrument_channel}

    pin_query.publish(valid_channels)
    num_missing_channels = [
        [len(expected_instrument_channels)] * len(row) for row in valid_channels
    ]
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nifgen_sessions()
    for session in sessions:
        session.close()
