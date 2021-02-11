import nidmm
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_nidmm_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
    sessions = {
        instrument_name: nidmm.Session(instrument_name, options={"Simulate": True})
        for instrument_name in instrument_names
    }
    for instrument_name, session in zip(instrument_names, sessions.values()):
        standalone_tsm_context.set_nidmm_session(instrument_name, session)
    yield sessions
    for session in sessions.values():
        session.close()


@pytest.mark.pin_map("nidmm.pinmap")
class TestNIDMM:

    @pytest.mark.parametrize("pin_map_instruments", (["DMM1", "DMM2", "DMM3"],))
    def test_get_all_nidmm_instrument_names(self, standalone_tsm_context, pin_map_instruments):
        instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in pin_map_instruments

    def test_set_nidmm_session(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
        for instrument_name in instrument_names:
            with nidmm.Session(instrument_name, options={"Simulate": True}) as session:
                standalone_tsm_context.set_nidmm_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    @pytest.mark.parametrize("expected_instr_names", (["DMM1", "DMM2", "DMM3"],))
    def test_get_all_nidmm_sessions(
        self, standalone_tsm_context, simulated_nidmm_sessions, expected_instr_names
    ):
        queried_sessions = standalone_tsm_context.get_all_nidmm_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(expected_instr_names)
        for queried_session, expected_instr_name in zip(queried_sessions, expected_instr_names):
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session is simulated_nidmm_sessions[expected_instr_name]

    @pytest.mark.parametrize("pin,expected_instr_name", [("SystemPin1", "DMM3")])
    def test_pin_to_nidmm_session(
        self, standalone_tsm_context, simulated_nidmm_sessions, pin, expected_instr_name
    ):
        pin_query_context, queried_session = standalone_tsm_context.pin_to_nidmm_session(pin)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidmm.Session)
        assert queried_session is simulated_nidmm_sessions[expected_instr_name]

    @pytest.mark.parametrize(
        "pins,expected_instr_names",
        [
            ("DUTPin1", ["DMM1", "DMM2"]),
            ("PinGroup1", ["DMM1", "DMM2", "DMM3"]),
            (["DUTPin1", "SystemPin1"], ["DMM1", "DMM2", "DMM3"]),
        ],
    )
    def test_pins_to_nidmm_sessions(
        self, standalone_tsm_context, simulated_nidmm_sessions, pins, expected_instr_names
    ):
        pin_query_context, queried_sessions = standalone_tsm_context.pins_to_nidmm_sessions(pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(expected_instr_names)
        for queried_session, expected_instr_name in zip(queried_sessions, expected_instr_names):
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session is simulated_nidmm_sessions[expected_instr_name]
