from typing import Tuple, Any
import os.path
import nidmm
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import *
from tests.fixtures import standalone_tsm_context

T = Tuple[SemiconductorModuleContext, Any]  # enable static type checking through type alias

pin_map_path = os.path.join(os.path.dirname(__file__), "nidmm.pinmap")
pin_map_instruments = ["DMM1", "DMM2", "DMM3"]
pin_map_dut_pins = {"DUTPin1": {0: "DMM1", 1: "DMM2"}}
pin_map_system_pins = {"SystemPin1": "DMM3"}
pin_map_pin_groups = {"PinGroup1": (pin_map_dut_pins, pin_map_system_pins, None)}


@pytest.mark.parametrize('standalone_tsm_context', [pin_map_path], indirect=True)
def test_get_all_nidmm_instrument_names(standalone_tsm_context: T):
    tsm, _ = standalone_tsm_context
    instrument_names = tsm.get_all_nidmm_instrument_names()
    assert len(instrument_names) == len(pin_map_instruments)
    assert set(instrument_names) == set(pin_map_instruments)


@pytest.mark.parametrize('standalone_tsm_context', [pin_map_path], indirect=True)
def test_set_nidmm_session(standalone_tsm_context: T):
    tsm, _ = standalone_tsm_context
    instrument_names = tsm.get_all_nidmm_instrument_names()
    for instrument_name in instrument_names:
        session = nidmm.Session(instrument_name, options={'Simulate': True})
        tsm.set_nidmm_session(instrument_name, session)
        assert SemiconductorModuleContext._sessions[id(session)] is session
        session.close()


@pytest.fixture
def add_instrument_sessions(standalone_tsm_context):
    tsm, _ = standalone_tsm_context
    instrument_names = tsm.get_all_nidmm_instrument_names()
    sessions = [nidmm.Session(instrument_name, options={'Simulate': True})
                for instrument_name in instrument_names]
    for instrument_name, session in zip(instrument_names, sessions):
        tsm.set_nidmm_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.parametrize('standalone_tsm_context', [pin_map_path], indirect=True)
def test_get_all_nidmm_sessions(standalone_tsm_context: T, add_instrument_sessions):
    tsm, _ = standalone_tsm_context
    queried_sessions = tsm.get_all_nidmm_sessions()
    assert len(queried_sessions) == len(add_instrument_sessions)
    assert set(queried_sessions) == set(add_instrument_sessions)


@pytest.mark.parametrize('standalone_tsm_context', [pin_map_path], indirect=True)
def test_pin_to_nidmm_session(standalone_tsm_context: T, add_instrument_sessions):
    tsm, _ = standalone_tsm_context
    for pin in pin_map_system_pins.keys():
        pin_query_context, session = tsm.pin_to_nidmm_session(pin)
        assert isinstance(pin_query_context, NIDmmSinglePinSingleSessionQueryContext)
        assert isinstance(session, nidmm.Session)
        assert session in add_instrument_sessions


@pytest.mark.parametrize('standalone_tsm_context', [pin_map_path], indirect=True)
def test_pin_nidmm_sessions(standalone_tsm_context: T, add_instrument_sessions):
    tsm, _ = standalone_tsm_context
    for pin_group in pin_map_pin_groups:
        pin_query_context, sessions = tsm.pin_to_nidcpower_sessions(pin_group)
        assert isinstance(pin_query_context, NIDmmSinglePinMultipleSessionQueryContext)
        assert all(isinstance(session, nidmm.Session) for session in sessions)
        assert all(session in add_instrument_sessions for session in sessions)

