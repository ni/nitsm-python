import niswitch
import pytest

from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import SinglePinSingleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import SinglePinMultipleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import MultiplePinSingleSessionQueryContext
from nitsm.codemoduleapi.pinquerycontexts import MultiplePinMultipleSessionQueryContext


@pytest.fixture
def simulated_custom_instrument_sessions(standalone_tsm_context):
    (instrument_names, channel_group_ids, _) = standalone_tsm_context.get_custom_instrument_names(
        TestCustomInstruments.pin_map_instrument_type_id
    )
    sessions = [
        niswitch.Session(instrument_name, topology="2567/Independent", simulate=True)
        for instrument_name in instrument_names
    ]
    for instrument_name, channel_group_id, session in zip(
        instrument_names, channel_group_ids, sessions
    ):
        standalone_tsm_context.set_custom_session(
            TestCustomInstruments.pin_map_instrument_type_id,
            instrument_name,
            channel_group_id,
            session,
        )
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("custom_instruments.pinmap")
class TestCustomInstruments:
    pin_map_instruments = ["PXI0::16"]
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]
    pin_map_pin_groups = ["PinGroup1"]
    pin_map_instrument_type_id = "Relay1_Id"

    def test_get_custom_instrument_names(self, standalone_tsm_context: SemiconductorModuleContext):
        (
            instrument_names,
            channel_group_ids,
            channel_lists,
        ) = standalone_tsm_context.get_custom_instrument_names(self.pin_map_instrument_type_id)
        assert isinstance(instrument_names, tuple)
        assert isinstance(channel_group_ids, tuple)
        assert isinstance(channel_lists, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        assert len(instrument_names) == len(channel_group_ids)
        assert len(instrument_names) == len(channel_lists)
        for instrument_name, channel_group_id, channel_list in zip(
            instrument_names, channel_group_ids, channel_lists
        ):
            assert isinstance(instrument_name, str)
            assert isinstance(channel_group_id, str)
            assert isinstance(channel_list, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_custom_session(self, standalone_tsm_context: SemiconductorModuleContext):
        (
            instrument_names,
            channel_group_ids,
            _,
        ) = standalone_tsm_context.get_custom_instrument_names(self.pin_map_instrument_type_id)
        for instrument_name, channel_group_id in zip(instrument_names, channel_group_ids):
            with niswitch.Session(
                instrument_name, topology="2567/Independent", simulate=True
            ) as session:
                standalone_tsm_context.set_custom_session(
                    self.pin_map_instrument_type_id, instrument_name, channel_group_id, session
                )
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_custom_sessions(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        (
            queried_sessions,
            queried_channel_group_ids,
            queried_channel_lists,
        ) = standalone_tsm_context.get_all_custom_sessions(self.pin_map_instrument_type_id)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_group_ids, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_custom_instrument_sessions)
        assert len(queried_sessions) == len(queried_channel_group_ids)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_group_id, queried_channel_list in zip(
            queried_sessions, queried_channel_group_ids, queried_channel_lists
        ):
            assert isinstance(queried_session, niswitch.Session)
            assert isinstance(queried_channel_group_id, str)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_custom_instrument_sessions

    def test_pin_to_custom_session(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        for system_pin in self.pin_map_system_pins:
            (
                pin_query_context,
                queried_session,
                queried_channel_group_id,
                queried_channel_list,
            ) = standalone_tsm_context.pin_to_custom_session(
                self.pin_map_instrument_type_id, system_pin
            )
            assert isinstance(pin_query_context, SinglePinSingleSessionQueryContext)
            assert isinstance(queried_session, niswitch.Session)
            assert isinstance(queried_channel_group_id, str)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_custom_instrument_sessions

    def test_pin_to_custom_sessions(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        for pin_group in self.pin_map_pin_groups:
            (
                pin_query_context,
                queried_sessions,
                queried_channel_group_ids,
                queried_channel_lists,
            ) = standalone_tsm_context.pin_to_custom_sessions(
                self.pin_map_instrument_type_id, pin_group
            )
            assert isinstance(pin_query_context, SinglePinMultipleSessionQueryContext)
            assert isinstance(queried_sessions, tuple)
            assert isinstance(queried_channel_group_ids, tuple)
            assert isinstance(queried_channel_lists, tuple)
            assert len(queried_sessions) == len(simulated_custom_instrument_sessions)
            assert len(queried_sessions) == len(queried_channel_group_ids)
            assert len(queried_sessions) == len(queried_channel_lists)
            for queried_session, queried_channel_group_id, queried_channel_list in zip(
                queried_sessions, queried_channel_group_ids, queried_channel_lists
            ):
                assert isinstance(queried_session, niswitch.Session)
                assert isinstance(queried_channel_group_id, str)
                assert isinstance(queried_channel_list, str)
                assert queried_session in simulated_custom_instrument_sessions

    def test_pins_to_custom_session(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_session,
            queried_channel_group_id,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_custom_session(self.pin_map_instrument_type_id, all_pins)
        assert isinstance(pin_query_context, MultiplePinSingleSessionQueryContext)
        assert isinstance(queried_session, niswitch.Session)
        assert isinstance(queried_channel_group_id, str)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_custom_instrument_sessions

    def test_pins_to_custom_sessions(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            queried_channel_group_ids,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_custom_sessions(
            self.pin_map_instrument_type_id, all_pins
        )
        assert isinstance(pin_query_context, MultiplePinMultipleSessionQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_group_ids, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_custom_instrument_sessions)
        assert len(queried_sessions) == len(queried_channel_group_ids)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_group_id, queried_channel_list in zip(
            queried_sessions, queried_channel_group_ids, queried_channel_lists
        ):
            assert isinstance(queried_session, niswitch.Session)
            assert isinstance(queried_channel_group_id, str)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_custom_instrument_sessions
