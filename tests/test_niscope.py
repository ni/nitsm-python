import niscope
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_niscope_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_niscope_instrument_names()
    sessions = [
        niscope.Session(instrument_name, options={"Simulate": True})
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_niscope_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("niscope.pinmap")
class TestNIScope:
    pin_map_instruments = ["Scope1,Scope2,Scope3"]
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]

    def test_get_all_niscope_instrument_names(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_all_niscope_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_niscope_session(self, standalone_tsm_context: SemiconductorModuleContext):
        instrument_names = standalone_tsm_context.get_all_niscope_instrument_names()
        for instrument_name in instrument_names:
            with niscope.Session(instrument_name, options={"Simulate": True}) as session:
                standalone_tsm_context.set_niscope_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_niscope_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        queried_sessions = standalone_tsm_context.get_all_niscope_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_niscope_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, niscope.Session)
            assert queried_session in simulated_niscope_sessions

    def test_pin_to_niscope_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pin_to_niscope_session("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, niscope.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_niscope_sessions

    def test_pin_to_niscope_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pin_to_niscope_sessions("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, niscope.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_niscope_sessions

    def test_pins_to_niscope_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_niscope_session(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, niscope.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_niscope_sessions

    def test_pins_to_niscope_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_niscope_sessions(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, niscope.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_niscope_sessions
