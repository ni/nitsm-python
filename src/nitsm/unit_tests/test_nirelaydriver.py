import niswitch
import pytest
from niswitch.enums import RelayAction
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_niswitch_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_relay_driver_module_names()
    sessions = [
        niswitch.Session(instrument_name, topology="2567/Independent", simulate=True)
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_relay_driver_niswitch_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nirelaydriver.pinmap")
class TestNIRelayDriver:
    pin_map_instruments = ["RelayDriver1", "RelayDriver2"]
    pin_map_site_relays = ["K0", "K1"]
    pin_map_system_relays = ["SystemRelay1"]
    pin_map_relay_groups = ["RelayGroup1"]

    def test_get_relay_driver_module_names(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_relay_driver_module_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_get_relay_names(self, standalone_tsm_context: SemiconductorModuleContext):
        site_relays, system_relays = standalone_tsm_context.get_relay_names()
        assert isinstance(site_relays, tuple)
        assert isinstance(system_relays, tuple)
        for site_relay, system_relay in zip(site_relays, system_relays):
            assert site_relay in self.pin_map_site_relays
            assert system_relay in self.pin_map_system_relays

    def test_set_relay_driver_niswitch_session(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_relay_driver_module_names()
        for instrument_name in instrument_names:
            with niswitch.Session(instrument_name, simulate=True) as session:
                standalone_tsm_context.set_relay_driver_niswitch_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_relay_driver_niswitch_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        queried_niswitch_sessions = standalone_tsm_context.get_all_relay_driver_niswitch_sessions()
        assert len(queried_niswitch_sessions) == len(simulated_niswitch_sessions)
        for queried_niswitch_session in queried_niswitch_sessions:
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relay_to_relay_driver_niswitch_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        for system_relay in self.pin_map_system_relays:
            (
                queried_niswitch_session,
                queried_niswitch_relay_names,
            ) = standalone_tsm_context.relay_to_relay_driver_niswitch_session(system_relay)
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert isinstance(queried_niswitch_relay_names, str)
            assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relay_to_relay_driver_niswitch_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        for relay_group in self.pin_map_relay_groups:
            (
                queried_niswitch_sessions,
                queried_niswitch_relay_names,
            ) = standalone_tsm_context.relay_to_relay_driver_niswitch_sessions(relay_group)
            assert isinstance(queried_niswitch_sessions, tuple)
            assert isinstance(queried_niswitch_relay_names, tuple)
            assert len(queried_niswitch_sessions) == len(queried_niswitch_relay_names)
            for queried_niswitch_session in queried_niswitch_sessions:
                assert isinstance(queried_niswitch_session, niswitch.Session)
                assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relays_to_relay_driver_niswitch_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        (
            queried_niswitch_session,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_session(self.pin_map_site_relays)
        assert isinstance(queried_niswitch_session, niswitch.Session)
        assert isinstance(queried_niswitch_relay_names, str)
        assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relays_to_relay_driver_niswitch_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        all_pins = self.pin_map_site_relays + self.pin_map_system_relays
        (
            queried_niswitch_sessions,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_sessions(all_pins)
        assert isinstance(queried_niswitch_sessions, tuple)
        assert isinstance(queried_niswitch_relay_names, tuple)
        assert len(queried_niswitch_sessions) == len(queried_niswitch_relay_names)
        for queried_niswitch_session in queried_niswitch_sessions:
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert queried_niswitch_session in simulated_niswitch_sessions

    def test_apply_relay_configuration(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        standalone_tsm_context.apply_relay_configuration("RelayConfiguration1", 0.0)
        pass

    def test_control_relay_single_action(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        standalone_tsm_context.control_relay_single_action("RelayGroup1", RelayAction.OPEN)
        pass

    def test_control_relays_single_action(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        all_pins = self.pin_map_site_relays + self.pin_map_system_relays
        standalone_tsm_context.control_relays_single_action(all_pins, RelayAction.OPEN)
        pass

    def test_control_relays_multiple_action(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        all_pins = self.pin_map_site_relays + self.pin_map_system_relays
        standalone_tsm_context.control_relays_multiple_action(
            all_pins, (RelayAction.CLOSE, RelayAction.CLOSE, RelayAction.OPEN)
        )
        pass
