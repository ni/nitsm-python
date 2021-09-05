import nidcpower
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext

OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "4141", "BoardType": "PXIe"}}


@nitsm.codemoduleapi.code_module
def open_sessions_channel_expansion(tsm_context: SemiconductorModuleContext):
    resource_strings = tsm_context.get_all_nidcpower_resource_strings()
    for resource_string in resource_strings:
        session = nidcpower.Session(resource_string, options=OPTIONS)
        tsm_context.set_nidcpower_session(resource_string, session)


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names, channel_strings = tsm_context.get_all_nidcpower_instrument_names()
    for instrument_name, channel_string in zip(instrument_names, channel_strings):
        session = nidcpower.Session(
            instrument_name, channel_string, options=OPTIONS, independent_channels=False
        )
        tsm_context.set_nidcpower_session_with_channel_string(
            instrument_name, channel_string, session
        )


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
    expected_channel_strings,
):
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(pins)
    expected_instrument_channels = set(zip(expected_instrument_names, expected_channel_strings))
    valid_channels = []

    for session, channel_string in zip(sessions, channel_strings):
        # call some methods on the session to ensure no errors
        pin_session = session.channels[channel_string]
        session.abort()
        pin_session.output_function = nidcpower.OutputFunction.DC_CURRENT
        pin_session.current_level = 10e-3
        pin_session.output_enabled = True
        pin_session.source_delay = 250e-6
        session.initiate()
        session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)
        pin_session.measure(nidcpower.MeasurementTypes.VOLTAGE)

        # check instrument channel we received is in the set of instrument channels we expected
        actual_instrument_channel = (session.io_resource_descriptor, channel_string)
        valid_channels.append(actual_instrument_channel in expected_instrument_channels)
        expected_instrument_channels -= {actual_instrument_channel}

    pin_query.publish(valid_channels)
    num_missing_channels = [len(expected_instrument_channels)] * len(sessions)
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidcpower_sessions()
    for session in sessions:
        session.close()
