import nidcpower
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext

OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "4162", "BoardType": "PXIe"}}


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    resource_strings = tsm_context.get_all_nidcpower_resource_strings()
    for resource_string in resource_strings:
        session = nidcpower.Session(resource_string, options=OPTIONS)
        tsm_context.set_nidcpower_session(resource_string, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_channel_strings,
):
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(pins)
    expected_instrument_channels = set(
        expected_channel_string.replace(" ", "")  # remove spaces
        for expected_channel_string in expected_channel_strings
    )
    valid_channels = []

    for session, channel_string in zip(sessions, channel_strings):
        # call some methods on the session to ensure no errors
        channel_session = session.channels[channel_string]
        channel_session.abort()
        channel_session.output_function = nidcpower.OutputFunction.DC_CURRENT
        channel_session.current_level = 1e-3
        channel_session.output_enabled = True
        channel_session.source_delay = 250e-6
        channel_session.initiate()
        channel_session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)
        channel_session.measure_multiple()

        # check instrument channels we received is in the set of instrument channels we expected
        actual_instrument_channels = session.io_resource_descriptor.replace(" ", "")
        channel_count = len(channel_string.split(","))
        valid_channels.append(
            [actual_instrument_channels in expected_instrument_channels] * channel_count
        )
        expected_instrument_channels -= {actual_instrument_channels}

    pin_query.publish(valid_channels)
    num_missing_channels = [
        [len(expected_instrument_channels)] * len(row) for row in valid_channels
    ]
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidcpower_sessions()
    for session in sessions:
        session.close()
