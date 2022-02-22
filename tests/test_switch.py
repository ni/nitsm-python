import pytest
from nitsm.tsmcontext import SemiconductorModuleContext


@pytest.fixture
def simulated_switch_sessions(standalone_tsm_context):
    switch_names = standalone_tsm_context.get_all_switch_names("")
    for switch_name in switch_names:
        standalone_tsm_context.set_switch_session(switch_name, switch_name, "")
    yield switch_names


@pytest.mark.pin_map("switch.pinmap")
class TestSwitch:
    switches = ["Multiplexer1"]

    def test_get_all_switch_names(self, standalone_tsm_context: SemiconductorModuleContext):
        switch_names = standalone_tsm_context.get_all_switch_names("")
        assert isinstance(switch_names, tuple)
        assert len(switch_names) == len(self.switches)
        for switch_name in switch_names:
            assert isinstance(switch_name, str)
            assert switch_name in self.switches

    def test_set_switch_session(self, standalone_tsm_context: SemiconductorModuleContext):
        switch_names = standalone_tsm_context.get_all_nidmm_instrument_names()
        for switch_name in switch_names:
            standalone_tsm_context.set_switch_session(switch_name, switch_name, "")
            assert SemiconductorModuleContext._sessions[id(switch_name)] is switch_name

    def test_get_all_switch_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_switch_sessions
    ):
        queried_sessions = standalone_tsm_context.get_all_switch_sessions("")
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_switch_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, str)
            assert queried_session in simulated_switch_sessions

    def test_pin_to_switch_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_switch_sessions
    ):
        tsm_contexts, sessions, switch_routes = standalone_tsm_context.pin_to_switch_sessions(
            "DUTPin1", ""
        )
        assert isinstance(tsm_contexts, tuple)
        assert isinstance(sessions, tuple)
        assert isinstance(switch_routes, tuple)
        assert len(tsm_contexts) == len(sessions)
        assert len(sessions) == len(switch_routes)
        for tsm_context, session, switch_route in zip(tsm_contexts, sessions, switch_routes):
            assert isinstance(tsm_context, SemiconductorModuleContext)
            assert len(tsm_context.site_numbers) == 1
            assert isinstance(session, str)
            assert session in simulated_switch_sessions
            assert isinstance(switch_route, str)
            assert switch_route == f"DUTPin1Site{tsm_context.site_numbers[0]}"
