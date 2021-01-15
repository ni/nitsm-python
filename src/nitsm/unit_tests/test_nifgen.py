import nifgen
import pytest

from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import NIFGenSinglePinSingleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIFGenSinglePinMultipleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIFGenMultiplePinSingleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIFGenMultiplePinMultipleSessionQueryContext


@pytest.fixture
def simulated_nifgen_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
    sessions = [
        nifgen.Session(
            instrument_name,
            options={"Simulate": True, "DriverSetup": {"Model": "5451", "BoardType": "PXIe"}},
        )
        for instrument_name in instrument_names
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
    pin_map_pin_groups = ["PinGroup1"]

    def test_get_all_nifgen_instrument_names(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_nifgen_session(self, standalone_tsm_context: SemiconductorModuleContext):
        instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
        for instrument_name in instrument_names:
            with nifgen.Session(
                instrument_name,
                options={"Simulate": True, "DriverSetup": {"Model": "5451", "BoardType": "PXIe"}},
            ) as session:
                standalone_tsm_context.set_nifgen_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_nifgen_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nifgen_sessions
    ):
        queried_sessions = standalone_tsm_context.get_all_nifgen_sessions()
        assert len(queried_sessions) == len(simulated_nifgen_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nifgen.Session)
            assert queried_session in simulated_nifgen_sessions

    def test_pin_to_nifgen_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nifgen_sessions
    ):
        for system_pin in self.pin_map_system_pins:
            (
                pin_query_context,
                queried_session,
                queried_channel_list,
            ) = standalone_tsm_context.pin_to_nifgen_session(system_pin)
            assert isinstance(pin_query_context, NIFGenSinglePinSingleSessionQueryContext)
            assert isinstance(queried_session, nifgen.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_nifgen_sessions

    def test_pin_to_nifgen_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nifgen_sessions
    ):
        for pin_group in self.pin_map_pin_groups:
            (
                pin_query_context,
                queried_sessions,
                queried_channel_lists,
            ) = standalone_tsm_context.pin_to_nifgen_sessions(pin_group)
            assert isinstance(pin_query_context, NIFGenSinglePinMultipleSessionQueryContext)
            assert isinstance(queried_sessions, tuple)
            assert isinstance(queried_channel_lists, tuple)
            assert len(queried_sessions) == len(simulated_nifgen_sessions)
            assert len(queried_sessions) == len(queried_channel_lists)
            for queried_session, queried_channel_list in zip(
                queried_sessions, queried_channel_lists
            ):
                assert isinstance(queried_session, nifgen.Session)
                assert isinstance(queried_channel_list, str)
                assert queried_session in simulated_nifgen_sessions

    def test_pins_to_nifgen_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nifgen_sessions
    ):
        all_pins = self.pin_map_system_pins
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nifgen_session(all_pins)
        assert isinstance(pin_query_context, NIFGenMultiplePinSingleSessionQueryContext)
        assert isinstance(queried_session, nifgen.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_nifgen_sessions

    def test_pins_to_nifgen_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nifgen_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nifgen_sessions(all_pins)
        assert isinstance(pin_query_context, NIFGenMultiplePinMultipleSessionQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_nifgen_sessions)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, nifgen.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_nifgen_sessions