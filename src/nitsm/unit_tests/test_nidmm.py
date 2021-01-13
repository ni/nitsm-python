import nidmm
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import NIDmmSinglePinSingleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIDmmSinglePinMultipleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIDmmMultiplePinMultipleSessionQueryContext


@pytest.fixture
def simulated_nidmm_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
    sessions = [
        nidmm.Session(instrument_name, options={"Simulate": True})
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nidmm_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map('nidmm.pinmap')
class TestNIDMM:
    pin_map_instruments = ["DMM1", "DMM2", "DMM3"]
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]
    pin_map_pin_groups = ["PinGroup1"]

    def test_get_all_nidmm_instrument_names(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_nidmm_session(self, standalone_tsm_context: SemiconductorModuleContext):
        instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
        for instrument_name in instrument_names:
            with nidmm.Session(instrument_name, options={"Simulate": True}) as session:
                standalone_tsm_context.set_nidmm_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_nidmm_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
    ):
        queried_sessions = standalone_tsm_context.get_all_nidmm_sessions()
        assert len(queried_sessions) == len(simulated_nidmm_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session in simulated_nidmm_sessions

    def test_pin_to_nidmm_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
    ):
        for system_pin in self.pin_map_system_pins:
            pin_query_context, queried_session = standalone_tsm_context.pin_to_nidmm_session(
                system_pin
            )
            assert isinstance(pin_query_context, NIDmmSinglePinSingleSessionQueryContext)
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session in simulated_nidmm_sessions

    def test_pin_to_nidmm_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
    ):
        for pin_group in self.pin_map_pin_groups:
            pin_query_context, queried_sessions = standalone_tsm_context.pin_to_nidmm_sessions(
                pin_group
            )
            assert isinstance(pin_query_context, NIDmmSinglePinMultipleSessionQueryContext)
            assert isinstance(queried_sessions, tuple)
            for queried_session in queried_sessions:
                assert isinstance(queried_session, nidmm.Session)
                assert queried_session in simulated_nidmm_sessions

    def test_pins_to_nidmm_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        pin_query_context, queried_sessions = standalone_tsm_context.pins_to_nidmm_sessions(
            all_pins
        )
        assert isinstance(pin_query_context, NIDmmMultiplePinMultipleSessionQueryContext)
        assert isinstance(queried_sessions, tuple)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session in simulated_nidmm_sessions
