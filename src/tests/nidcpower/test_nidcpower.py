from typing import Tuple, Any
import nidcpower
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import *
from tests.fixtures import standalone_tsm_context

T = Tuple[SemiconductorModuleContext, Any]  # enable static type checking through type alias

pin_map_path = r'C:\Users\Sean Moore\Projects\nitsm-python\src\tests\nidcpower.pinmap'


@pytest.mark.parametrize('standalone_tsm_context', [pin_map_path], indirect=True)
def test_get_all_nidcpower_instrument_names(standalone_tsm_context: T):
    tsm, _ = standalone_tsm_context
    instrument_names, channel_strings = tsm.get_all_nidcpower_instrument_names()
    assert len(instrument_names) == len(channel_strings)
    assert len(instrument_names) == 3
    assert 'DCPower1' in instrument_names
    assert 'DCPower2' in instrument_names
    dcpower1_instances = filter(lambda instr_name: instr_name == 'DCPower1', instrument_names)
    assert len(list(dcpower1_instances)) == 1
    dcpower2_instances = filter(lambda instr_name: instr_name == 'DCPower2', instrument_names)
    assert len(list(dcpower2_instances)) == 2


@pytest.fixture
def add_instrument_sessions(standalone_tsm_context):
    tsm, _ = standalone_tsm_context
    instrument_names, channel_strings = tsm.get_all_nidcpower_instrument_names()
    sessions = [nidcpower.Session(instrument_name, channel_string, options={'Simulate': True}) for
                instrument_name, channel_string in zip(instrument_names, channel_strings)]
    for session, instrument_name, channel_string in zip(sessions, instrument_names, channel_strings):
        tsm.set_nidcpower_session(instrument_name, channel_string, session)
    return sessions, instrument_names, channel_strings


@pytest.mark.parametrize('standalone_tsm_context', [pin_map_path], indirect=True)
def test_set_nidcpower_session(add_instrument_sessions):
    sessions, instrument_names, channel_strings = add_instrument_sessions
    for session, instrument_name, channel_string in zip(sessions, instrument_names, channel_strings):
        assert id(session) in SemiconductorModuleContext._sessions
        assert SemiconductorModuleContext._sessions[id(session)] is session


@pytest.mark.parametrize('standalone_tsm_context', [pin_map_path], indirect=True)
def test_pin_to_nidcpower_session(standalone_tsm_context: T, add_instrument_sessions):
    tsm, _ = standalone_tsm_context
    sessions, instrument_names, channel_strings = add_instrument_sessions
    instr_set = set(zip(sessions, channel_strings))
    for dut_pin in ['DUTPin1', 'DUTPin2', 'DUTPin3']:
        pin_query_context, session, channel_string = tsm.pin_to_nidcpower_session(dut_pin)
        assert isinstance(pin_query_context, NIDCPowerSinglePinSingleSessionQueryContext)
        assert isinstance(session, nidcpower.Session)
        assert (session, channel_string) in instr_set
