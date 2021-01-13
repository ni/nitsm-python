from typing import Tuple, Any
import os.path
import nidcpower
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import *
from tests.fixtures import standalone_tsm_context

T = Tuple[SemiconductorModuleContext, Any]  # enable static type checking through type alias

pin_map_path = os.path.join(os.path.dirname(__file__), "nidcpower.pinmap")
pin_map_instruments = {"DCPower1": 1, "DCPower2": 2, "DCPower3": 1, "DCPower4": 2, "DCPower5": 1}
pin_map_dut_pins = {
    "DUTPin1": {0: ("DCPower1", "0"), 1: ("DCPower3", "0")},
    "DUTPin2": {0: ("DCPower2", "0"), 1: ("DCPower4", "0")},
    "DUTPin3": {0: ("DCPower2", "1"), 1: ("DCPower4", "1")},
}
pin_map_system_pins = {"SystemPin1": ("DCPower5", "0")}
pin_map_pin_groups = {"PinGroup1": (pin_map_dut_pins, None, None)}


@pytest.mark.parametrize("standalone_tsm_context", [pin_map_path], indirect=True)
def test_get_all_nidcpower_instrument_names(standalone_tsm_context: T):
    tsm, _ = standalone_tsm_context
    instrument_names, channel_strings = tsm.get_all_nidcpower_instrument_names()
    assert len(instrument_names) == len(channel_strings)
    assert len(instrument_names) == sum(pin_map_instruments.values())

    pin_map_instrument_channel_pairs = [
        pair for sublist in pin_map_dut_pins.values() for pair in sublist
    ]
    pin_map_instrument_channel_pairs.extend(pin_map_system_pins.values())

    instrument_channel_pairs = list(zip(instrument_names, channel_strings))
    for instrument_channel_pair in instrument_channel_pairs:
        assert instrument_channel_pair in pin_map_instrument_channel_pairs
        instrument_channel_pair_instances = list(
            filter(
                lambda instr_chan_pair: instr_chan_pair == instrument_channel_pair,
                pin_map_instrument_channel_pairs,
            )
        )
        assert len(instrument_channel_pair_instances) == 1


@pytest.mark.parametrize("standalone_tsm_context", [pin_map_path], indirect=True)
def test_set_nidcpower_session(add_instrument_sessions):
    sessions, *_ = add_instrument_sessions
    for session in sessions:
        assert SemiconductorModuleContext._sessions[id(session)] is session


@pytest.fixture
def add_instrument_sessions(standalone_tsm_context):
    tsm, _ = standalone_tsm_context
    instrument_names, channel_strings = tsm.get_all_nidcpower_instrument_names()
    sessions = [
        nidcpower.Session(instrument_name, channel_string, options={"Simulate": True})
        for instrument_name, channel_string in zip(instrument_names, channel_strings)
    ]
    for session, instrument_name, channel_string in zip(
        sessions, instrument_names, channel_strings
    ):
        tsm.set_nidcpower_session(instrument_name, channel_string, session)
    return sessions, instrument_names, channel_strings


@pytest.mark.parametrize("standalone_tsm_context", [pin_map_path], indirect=True)
def test_get_all_nidcpower_sessions(standalone_tsm_context: T, add_instrument_sessions):
    tsm, _ = standalone_tsm_context
    sessions = tsm.get_all_nidcpower_sessions()
    assert len(sessions) == sum(pin_map_instruments.values())
    assert all(isinstance(session, nidcpower.Session) for session in sessions)


@pytest.mark.parametrize("standalone_tsm_context", [pin_map_path], indirect=True)
def test_pin_to_nidcpower_session(standalone_tsm_context: T, add_instrument_sessions):
    tsm, _ = standalone_tsm_context
    sessions, _, channel_strings = add_instrument_sessions
    session_channel_pairs = set(zip(sessions, channel_strings))
    for system_pin in pin_map_system_pins:
        pin_query_context, queried_session, queried_channel_string = tsm.pin_to_nidcpower_session(
            system_pin
        )
        assert isinstance(pin_query_context, NIDCPowerSinglePinSingleSessionQueryContext)
        assert isinstance(queried_session, nidcpower.Session)
        assert (queried_session, queried_channel_string) in session_channel_pairs


@pytest.mark.parametrize("standalone_tsm_context", [pin_map_path], indirect=True)
def test_pin_to_nidcpower_sessions(standalone_tsm_context: T, add_instrument_sessions):
    tsm, _ = standalone_tsm_context
    sessions, _, channel_strings = add_instrument_sessions
    session_channel_pairs = set(zip(sessions, channel_strings))

    for pin_group in pin_map_pin_groups:
        (
            pin_query_context,
            queried_sessions,
            queried_channel_strings,
        ) = tsm.pin_to_nidcpower_sessions(pin_group)
        assert isinstance(pin_query_context, NIDCPowerSinglePinMultipleSessionQueryContext)
        assert len(queried_sessions) == len(queried_channel_strings)
        assert len(queried_sessions) == len(pin_map_pin_groups[pin_group]) * pin_map_num_sites

        for queried_session, queried_channel_string in zip(
            queried_sessions, queried_channel_strings
        ):
            assert isinstance(queried_session, nidcpower.Session)
            assert (queried_session, queried_channel_string) in session_channel_pairs


@pytest.mark.parametrize("standalone_tsm_context", [pin_map_path], indirect=True)
def test_pins_to_nidcpower_sessions(standalone_tsm_context: T, add_instrument_sessions):
    tsm, _ = standalone_tsm_context
    sessions, _, channel_strings = add_instrument_sessions
    session_channel_pairs = set(zip(sessions, channel_strings))

    pin_query_context, queried_sessions, queried_channel_strings = tsm.pins_to_nidcpower_sessions(
        list(pin_map_dut_pins.keys())
    )
    assert isinstance(pin_query_context, NIDCPowerMultiplePinMultipleSessionQueryContext)
    assert len(queried_sessions) == len(queried_channel_strings)

    pin_map_instrument_channel_pairs = [
        pair for sublist in pin_map_dut_pins.values() for pair in sublist
    ]
    assert len(queried_sessions) == len(pin_map_instrument_channel_pairs)

    instrument_names = set(pair[0] for pair in pin_map_instrument_channel_pairs)
    assert len(queried_sessions) == sum(
        [pin_map_instruments[instrument_name] for instrument_name in instrument_names]
    )

    for queried_session, queried_channel_string in zip(queried_sessions, queried_channel_strings):
        assert isinstance(queried_session, nidcpower.Session)
        assert (queried_session, queried_channel_string) in session_channel_pairs
