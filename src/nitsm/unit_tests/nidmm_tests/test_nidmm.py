import os.path
import nidmm
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import NIDmmSinglePinSingleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIDmmSinglePinMultipleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIDmmMultiplePinMultipleSessionQueryContext


pin_map_path = os.path.join(os.path.dirname(__file__), "nidmm.pinmap")
pin_map_instruments = ["DMM1", "DMM2", "DMM3"]
pin_map_dut_pins = {"DUTPin1": {0: "DMM1", 1: "DMM2"}}
pin_map_system_pins = {"SystemPin1": "DMM3"}
pin_map_pin_groups = {"PinGroup1": (pin_map_dut_pins, pin_map_system_pins, None)}


@pytest.mark.pin_map(pin_map_path)
def test_get_all_nidmm_instrument_names(standalone_tsm_context: SemiconductorModuleContext):
    instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
    assert len(instrument_names) == len(pin_map_instruments)
    assert set(instrument_names) == set(pin_map_instruments)


@pytest.mark.pin_map(pin_map_path)
def test_set_nidmm_session(standalone_tsm_context: SemiconductorModuleContext):
    instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
    for instrument_name in instrument_names:
        session = nidmm.Session(instrument_name, options={"Simulate": True})
        standalone_tsm_context.set_nidmm_session(instrument_name, session)
        assert SemiconductorModuleContext._sessions[id(session)] is session
        session.close()


@pytest.mark.pin_map(pin_map_path)
def test_get_all_nidmm_sessions(
    standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
):
    queried_sessions = standalone_tsm_context.get_all_nidmm_sessions()
    assert len(queried_sessions) == len(simulated_nidmm_sessions)
    assert set(queried_sessions) == set(simulated_nidmm_sessions)


@pytest.mark.pin_map(pin_map_path)
def test_pin_to_nidmm_session(
    standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
):
    for pin in pin_map_system_pins.keys():
        pin_query_context, queried_session = standalone_tsm_context.pin_to_nidmm_session(pin)
        assert isinstance(pin_query_context, NIDmmSinglePinSingleSessionQueryContext)
        assert isinstance(queried_session, nidmm.Session)
        assert queried_session in simulated_nidmm_sessions


@pytest.mark.pin_map(pin_map_path)
def test_pin_to_nidmm_sessions(
    standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
):
    for pin_group in pin_map_pin_groups:
        pin_query_context, queried_sessions = \
            standalone_tsm_context.pin_to_nidcpower_sessions(pin_group)
        assert isinstance(pin_query_context, NIDmmSinglePinMultipleSessionQueryContext)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session in simulated_nidmm_sessions


@pytest.mark.pin_map(pin_map_path)
def test_pin_to_nidmm_sessions(
        standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
):
    all_pins = list(pin_map_dut_pins.keys()) + list(pin_map_system_pins.keys())
    pin_query_context, queried_sessions = standalone_tsm_context.pins_to_nidmm_sessions(all_pins)
    assert isinstance(pin_query_context, NIDmmMultiplePinMultipleSessionQueryContext)
    for queried_session in queried_sessions:
        assert isinstance(queried_session, nidmm.Session)
        assert queried_session in simulated_nidmm_sessions
