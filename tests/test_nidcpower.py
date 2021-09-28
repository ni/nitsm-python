import nidcpower
import pytest
from nitsm.pinquerycontexts import PinQueryContext

OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "4162"}}


@pytest.fixture
def simulated_nidcpower_sessions(standalone_tsm_context):
    resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
    sessions = [
        nidcpower.Session(resource_string, options=OPTIONS) for resource_string in resource_strings
    ]
    for resource_string, session in zip(resource_strings, sessions):
        standalone_tsm_context.set_nidcpower_session(resource_string, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nidcpower.pinmap")
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
class TestNIDCPower:
    def test_get_all_nidcpower_resource_strings(self, standalone_tsm_context):
        resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
        assert isinstance(resource_strings, tuple)
        for resource_string in resource_strings:
            assert isinstance(resource_string, str)

    def test_set_nidcpower_session(self, standalone_tsm_context):
        resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
        for resource_string in resource_strings:
            with nidcpower.Session(resource_string, options=OPTIONS) as session:
                standalone_tsm_context.set_nidcpower_session(resource_string, session)
                assert standalone_tsm_context._sessions[id(session)] is session

    def test_get_all_nidcpower_sessions(self, standalone_tsm_context, simulated_nidcpower_sessions):
        queried_sessions = standalone_tsm_context.get_all_nidcpower_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_nidcpower_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidcpower.Session)
            assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_session_single_pin(
        self, standalone_tsm_context, simulated_nidcpower_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_string,
        ) = standalone_tsm_context.pins_to_nidcpower_session("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidcpower.Session)
        assert isinstance(queried_channel_string, str)
        assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_session_multiple_pins(
        self, standalone_tsm_context, simulated_nidcpower_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_string,
        ) = standalone_tsm_context.pins_to_nidcpower_session(["DUTPin1", "DUTPin2"])
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidcpower.Session)
        assert isinstance(queried_channel_string, str)
        assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_sessions_single_pin(
        self, standalone_tsm_context, simulated_nidcpower_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_strings,
        ) = standalone_tsm_context.pins_to_nidcpower_sessions("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_strings, tuple)
        assert len(queried_sessions) == len(queried_channel_strings)
        for queried_session, queried_channel_string in zip(
            queried_sessions, queried_channel_strings
        ):
            assert isinstance(queried_session, nidcpower.Session)
            assert isinstance(queried_channel_string, str)
            assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_sessions_multiple_pins(
        self, standalone_tsm_context, simulated_nidcpower_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_strings,
        ) = standalone_tsm_context.pins_to_nidcpower_sessions(["DUTPin1", "DUTPin3"])
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_strings, tuple)
        assert len(queried_sessions) == len(queried_channel_strings)
        for queried_session, queried_channel_string in zip(
            queried_sessions, queried_channel_strings
        ):
            assert isinstance(queried_session, nidcpower.Session)
            assert isinstance(queried_channel_string, str)
            assert queried_session in simulated_nidcpower_sessions
