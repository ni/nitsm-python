import pytest
import niswitch
from niswitch.enums import RelayAction, RelayPosition
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_niswitch_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_relay_driver_module_names()
    sessions = [
        niswitch.Session("", topology="2567/Independent", simulate=True) for _ in instrument_names
    ]  # resource name must be empty string to simulate an niswitch
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_relay_driver_niswitch_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


def assert_relay_positions(standalone_tsm_context, pin_map_relays, relay_position):
    (
        niswitch_sessions,
        niswitch_relay_names,
    ) = standalone_tsm_context.relays_to_relay_driver_niswitch_sessions(pin_map_relays)
    for niswitch_session, relay_names in zip(niswitch_sessions, niswitch_relay_names):
        for relay_name in relay_names.split(","):
            assert niswitch_session.get_relay_position(relay_name) == relay_position


@pytest.mark.pin_map("nirelaydriver.pinmap")
class TestNIRelayDriver:
    pin_map_instruments = ["RelayDriver1", "RelayDriver2"]
    pin_map_site_relays = ["SiteRelay1", "SiteRelay2"]
    pin_map_system_relays = ["SystemRelay1"]

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
        for site_relay in site_relays:
            assert isinstance(site_relay, str)
            assert site_relay in self.pin_map_site_relays
        for system_relay in system_relays:
            assert isinstance(system_relay, str)
            assert system_relay in self.pin_map_system_relays

    def test_set_relay_driver_niswitch_session(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_relay_driver_module_names()
        for instrument_name in instrument_names:
            with niswitch.Session("", topology="2567/Independent", simulate=True) as session:
                standalone_tsm_context.set_relay_driver_niswitch_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_relay_driver_niswitch_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        queried_niswitch_sessions = standalone_tsm_context.get_all_relay_driver_niswitch_sessions()
        assert isinstance(queried_niswitch_sessions, tuple)
        assert len(queried_niswitch_sessions) == len(simulated_niswitch_sessions)
        for queried_niswitch_session in queried_niswitch_sessions:
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relay_to_relay_driver_niswitch_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        (
            queried_niswitch_session,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relay_to_relay_driver_niswitch_session("SystemRelay1")
        assert isinstance(queried_niswitch_session, niswitch.Session)
        assert isinstance(queried_niswitch_relay_names, str)
        assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relay_to_relay_driver_niswitch_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        (
            queried_niswitch_sessions,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relay_to_relay_driver_niswitch_sessions("RelayGroup1")
        assert isinstance(queried_niswitch_sessions, tuple)
        assert isinstance(queried_niswitch_relay_names, tuple)
        assert len(queried_niswitch_sessions) == len(queried_niswitch_relay_names)
        for queried_niswitch_session, queried_relay_name in zip(
            queried_niswitch_sessions, queried_niswitch_relay_names
        ):
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert isinstance(queried_relay_name, str)
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
        all_relays = self.pin_map_site_relays + self.pin_map_system_relays
        (
            queried_niswitch_sessions,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_sessions(all_relays)
        assert isinstance(queried_niswitch_sessions, tuple)
        assert isinstance(queried_niswitch_relay_names, tuple)
        assert len(queried_niswitch_sessions) == len(queried_niswitch_relay_names)
        for queried_niswitch_session, queried_relay_name in zip(
            queried_niswitch_sessions, queried_niswitch_relay_names
        ):
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert isinstance(queried_relay_name, str)
            assert queried_niswitch_session in simulated_niswitch_sessions

    def test_apply_relay_configuration(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        standalone_tsm_context.apply_relay_configuration("RelayConfiguration1")
        assert_relay_positions(
            standalone_tsm_context, self.pin_map_site_relays, RelayPosition.CLOSED
        )
        assert_relay_positions(
            standalone_tsm_context, self.pin_map_system_relays, RelayPosition.OPEN
        )

    def test_control_relay_single_action_open_system_relay(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        (
            niswitch_session,
            niswitch_relay_name,
        ) = standalone_tsm_context.relay_to_relay_driver_niswitch_session("SystemRelay1")
        standalone_tsm_context.control_relay_single_action("SystemRelay1", RelayAction.OPEN)
        assert niswitch_session.get_relay_position(niswitch_relay_name) == RelayPosition.OPEN

    def test_control_relay_single_action_close_system_relay(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        (
            niswitch_session,
            niswitch_relay_name,
        ) = standalone_tsm_context.relay_to_relay_driver_niswitch_session("SystemRelay1")
        standalone_tsm_context.control_relay_single_action("SystemRelay1", RelayAction.CLOSE)
        assert niswitch_session.get_relay_position(niswitch_relay_name) == RelayPosition.CLOSED

    def test_control_relays_single_action_open_all_site_relays(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        standalone_tsm_context.control_relays_single_action(
            self.pin_map_site_relays, RelayAction.OPEN
        )
        assert_relay_positions(standalone_tsm_context, self.pin_map_site_relays, RelayPosition.OPEN)

    def test_control_relays_single_action_close_all_site_relays(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        standalone_tsm_context.control_relays_single_action(
            self.pin_map_site_relays, RelayAction.CLOSE
        )
        assert_relay_positions(
            standalone_tsm_context, self.pin_map_site_relays, RelayPosition.CLOSED
        )

    def test_control_relays_multiple_action_open_all_site_relays(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        standalone_tsm_context.control_relays_multiple_action(
            self.pin_map_site_relays, [RelayAction.OPEN] * len(self.pin_map_site_relays)
        )
        assert_relay_positions(standalone_tsm_context, self.pin_map_site_relays, RelayPosition.OPEN)

    def test_control_relays_multiple_action_close_all_site_relays(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        standalone_tsm_context.control_relays_multiple_action(
            self.pin_map_site_relays, [RelayAction.CLOSE] * len(self.pin_map_site_relays)
        )
        assert_relay_positions(
            standalone_tsm_context, self.pin_map_site_relays, RelayPosition.CLOSED
        )

    def test_control_relays_multiple_action_mixed_site_relay_positions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        relay_actions = [
            RelayAction.OPEN if i % 2 else RelayAction.CLOSE
            for i in range(len(self.pin_map_site_relays))
        ]
        standalone_tsm_context.control_relays_multiple_action(
            self.pin_map_site_relays, relay_actions
        )
        for pin_map_site_relay, relay_action in zip(self.pin_map_site_relays, relay_actions):
            relay_position = (
                RelayPosition.OPEN if relay_action == RelayAction.OPEN else RelayPosition.CLOSED
            )
            assert_relay_positions(
                standalone_tsm_context, [pin_map_site_relay], relay_position
            )
