import nidcpower
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.pinquerycontexts import NIDCPowerSinglePinSingleSessionQueryContext
from nitsm.pinquerycontexts import NIDCPowerSinglePinMultipleSessionQueryContext
from nitsm.pinquerycontexts import NIDCPowerMultiplePinSingleSessionQueryContext
from nitsm.pinquerycontexts import NIDCPowerMultiplePinMultipleSessionQueryContext


@pytest.fixture
def simulated_nidcpower_sessions(standalone_tsm_context):
    instrument_names, channel_strings = standalone_tsm_context.get_all_nidcpower_instrument_names()
    sessions = [
        nidcpower.Session(instrument_name, channel_string, options={"Simulate": True})
        for instrument_name, channel_string in zip(instrument_names, channel_strings)
    ]
    for instrument_name, channel_string, session in zip(
        instrument_names, channel_strings, sessions
    ):
        standalone_tsm_context.set_nidcpower_session(instrument_name, channel_string, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nidcpower.pinmap")
class TestNIDCPower:
    pin_map_instruments = ["DCPower1", "DCPower2", "DCPower3", "DCPower4", "DCPower5"]
    pin_map_dut_pins = ["DUTPin1", "DUTPin2", "DUTPin3"]
    pin_map_system_pins = ["SystemPin1"]

    def test_get_all_nidcpower_instrument_names(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        (
            instrument_names,
            channel_strings,
        ) = standalone_tsm_context.get_all_nidcpower_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert isinstance(channel_strings, tuple)
        assert len(instrument_names) == len(channel_strings)
        for instrument_name, channel_string in zip(instrument_names, channel_strings):
            assert isinstance(instrument_name, str)
            assert isinstance(channel_string, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_nidcpower_session(self, standalone_tsm_context: SemiconductorModuleContext):
        (
            instrument_names,
            channel_strings,
        ) = standalone_tsm_context.get_all_nidcpower_instrument_names()
        for instrument_name, channel_string in zip(instrument_names, channel_strings):
            with nidcpower.Session(
                instrument_name, channel_string, options={"Simulate": True}
            ) as session:
                standalone_tsm_context.set_nidcpower_session(
                    instrument_name, channel_string, session
                )
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_nidcpower_sessions(self, standalone_tsm_context, simulated_nidcpower_sessions):
        queried_sessions = standalone_tsm_context.get_all_nidcpower_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_nidcpower_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidcpower.Session)
            assert queried_session in simulated_nidcpower_sessions

    def test_pin_to_nidcpower_session(self, standalone_tsm_context, simulated_nidcpower_sessions):
        (
            pin_query_context,
            queried_session,
            queried_channel_string,
        ) = standalone_tsm_context.pin_to_nidcpower_session("SystemPin1")
        assert isinstance(pin_query_context, NIDCPowerSinglePinSingleSessionQueryContext)
        assert isinstance(queried_session, nidcpower.Session)
        assert isinstance(queried_channel_string, str)
        assert queried_session in simulated_nidcpower_sessions

    def test_pin_to_nidcpower_sessions(self, standalone_tsm_context, simulated_nidcpower_sessions):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_strings,
        ) = standalone_tsm_context.pin_to_nidcpower_sessions("PinGroup1")
        assert isinstance(pin_query_context, NIDCPowerSinglePinMultipleSessionQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_strings, tuple)
        assert len(queried_sessions) == len(queried_channel_strings)
        for queried_session, queried_channel_string in zip(
            queried_sessions, queried_channel_strings
        ):
            assert isinstance(queried_session, nidcpower.Session)
            assert isinstance(queried_channel_string, str)
            assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_sessions(self, standalone_tsm_context, simulated_nidcpower_sessions):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            queried_channel_strings,
        ) = standalone_tsm_context.pins_to_nidcpower_sessions(all_pins)
        assert isinstance(pin_query_context, NIDCPowerMultiplePinMultipleSessionQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_strings, tuple)
        assert len(queried_sessions) == len(queried_channel_strings)
        for queried_session, queried_channel_string in zip(
            queried_sessions, queried_channel_strings
        ):
            assert isinstance(queried_session, nidcpower.Session)
            assert isinstance(queried_channel_string, str)
            assert queried_session in simulated_nidcpower_sessions


@pytest.fixture
def simulated_nidcpower_sessions_with_resource_strings(standalone_tsm_context):
    resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
    sessions = [
        nidcpower.Session(resource_string, options={"Simulate": True})
        for resource_string in resource_strings
    ]
    for resource_string, session in zip(resource_strings, sessions):
        standalone_tsm_context.set_nidcpower_session_with_resource_string(resource_string, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nidcpower_channelgroups.pinmap")
class TestNIDCPowerChannelGroups:
    pin_map_channel_group_pins = ["DUTPin1", "DUTPin2", "DUTPin3"]

    def test_get_all_nidcpower_resource_strings(self, standalone_tsm_context):
        resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
        assert isinstance(resource_strings, tuple)
        for resource_string in resource_strings:
            assert isinstance(resource_string, str)

    def test_set_nidcpower_session_with_resource_string(self, standalone_tsm_context):
        resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
        for resource_string in resource_strings:
            with nidcpower.Session(resource_string, options={"Simulate": True}) as session:
                standalone_tsm_context.set_nidcpower_session_with_resource_string(
                    resource_string, session
                )
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_pins_to_nidcpower_session(
        self, standalone_tsm_context, simulated_nidcpower_sessions_with_resource_strings
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_string,
        ) = standalone_tsm_context.pins_to_nidcpower_session(self.pin_map_channel_group_pins)
        assert isinstance(pin_query_context, NIDCPowerMultiplePinSingleSessionQueryContext)
        assert isinstance(queried_session, nidcpower.Session)
        assert isinstance(queried_channel_string, str)
        assert queried_session in simulated_nidcpower_sessions_with_resource_strings
