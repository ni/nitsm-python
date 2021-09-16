from typing import TYPE_CHECKING
import nidigital
import pytest

if TYPE_CHECKING:
    from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_nidigital_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
    sessions = [
        nidigital.Session(
            instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
        )
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nidigital_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("pinquerycontext.pinmap")
class TestPinQueryContext:
    @pytest.mark.usefixtures("simulated_nidigital_sessions")
    def test_get_session_and_channel_index(
        self, standalone_tsm_context: "SemiconductorModuleContext"
    ):
        pin_query_context, _, _ = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu(
            ["DUTPin2", "DUTPin1"]
        )
        session_index, channel_index = pin_query_context.get_session_and_channel_index(1, "DUTPin1")
        assert session_index == 1
        assert channel_index == 1
