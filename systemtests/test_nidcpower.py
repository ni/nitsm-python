import nitsm.codemoduleapi
import nidcpower
from nitsm.codemoduleapi import SemiconductorModuleContext


class NIDCPowerSystemTest:

    OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "4141", "BoardType": "PXIe"}}

    @staticmethod
    @nitsm.codemoduleapi.code_module
    def open_sessions_channel_expansion(tsm_context: SemiconductorModuleContext):
        resource_names = tsm_context.get_all_nidcpower_resource_strings()
        sessions = [
            nidcpower.Session(resource_name, options=NIDCPowerSystemTest.OPTIONS)
            for resource_name in resource_names
        ]
        for resource_name, session in zip(resource_names, sessions):
            tsm_context.set_nidcpower_session(resource_name, session)

    @staticmethod
    @nitsm.codemoduleapi.code_module
    def open_sessions(tsm_context: SemiconductorModuleContext):
        instrument_names, channel_strings = tsm_context.get_all_nidcpower_instrument_names()
        for instrument_name, channel_string in zip(instrument_names, channel_strings):
            session = nidcpower.Session(instrument_name, channel_string, options=NIDCPowerSystemTest.OPTIONS)
            tsm_context.set_nidcpower_session(instrument_name, channel_string, session)

    @staticmethod
    @nitsm.codemoduleapi.code_module
    def close_sessions(tsm_context: SemiconductorModuleContext):
        sessions = tsm_context.get_all_nidcpower_sessions()
        for session in sessions:
            session.close()

    @staticmethod
    @nitsm.codemoduleapi.code_module
    def measure(tsm_context: SemiconductorModuleContext, pins, expected_instrument_names, expected_channel_strings):
        pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(pins)

        expected_instrument_channels = list(zip(expected_instrument_names, expected_channel_strings))
        valid_channels = []
        for session, channel_string in zip(sessions, channel_strings):
            NIDCPowerSystemTest._call_dcpower_methods(session, channel_string)

            actual_instrument_channel = (session.io_resource_descriptor, channel_string)
            actual_channel_is_valid = actual_instrument_channel in expected_instrument_channels
            if actual_channel_is_valid:
                expected_instrument_channels.remove(actual_instrument_channel)
            valid_channels.append(actual_channel_is_valid)

        num_missing_channels = [len(expected_instrument_channels)] * len(valid_channels)
        pin_query.publish(num_missing_channels, "NumMissing")
        pin_query.publish(valid_channels)

    @staticmethod
    def _call_dcpower_methods(session, channel_string):
        pin_session = session.channels[channel_string]

        # call some methods on the session to ensure no errors
        session.abort()
        pin_session.output_function = nidcpower.OutputFunction.DC_CURRENT
        pin_session.current_level = 10e-3
        pin_session.output_enabled = True
        pin_session.source_delay = 250e-6
        session.initiate()
        session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)
        pin_session.measure(nidcpower.MeasurementTypes.VOLTAGE)
