import nifgen
import pytest
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_nifgen_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
    sessions = [
        nifgen.Session(
            "", options={"Simulate": True, "driver_setup": {"Model": "5442", "BoardType": "PXIe"}}
        )
        for _ in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nifgen_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nifgen.pinmap")
class TestNIFGen:
    pin_map_instruments = ["FGen1", "FGen2"]
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1", "SystemPin2"]

    def test_get_all_nifgen_instrument_names(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_nifgen_session(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
        for instrument_name in instrument_names:
            with nifgen.Session("", options={"Simulate": True}) as session:
                standalone_tsm_context.set_nifgen_session(instrument_name, session)
                assert standalone_tsm_context._sessions[id(session)] is session

    def test_get_all_nifgen_sessions(self, standalone_tsm_context, simulated_nifgen_sessions):
        queried_sessions = standalone_tsm_context.get_all_nifgen_sessions()
        assert len(queried_sessions) == len(simulated_nifgen_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nifgen.Session)
            assert queried_session in simulated_nifgen_sessions

    def test_pin_to_nifgen_session_single_pin(
        self, standalone_tsm_context, simulated_nifgen_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nifgen_session("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nifgen.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_nifgen_sessions

    def test_pins_to_nifgen_session_muliple_pins(
        self, standalone_tsm_context, simulated_nifgen_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nifgen_session(self.pin_map_system_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nifgen.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_nifgen_sessions

    def test_pins_to_nifgen_sessions_single_pin(
        self, standalone_tsm_context, simulated_nifgen_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nifgen_sessions("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_nifgen_sessions)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, nifgen.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_nifgen_sessions

    def test_pins_to_nifgen_sessions_multiple_pins(
        self, standalone_tsm_context, simulated_nifgen_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nifgen_sessions(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_nifgen_sessions)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, nifgen.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_nifgen_sessions
