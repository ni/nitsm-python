from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
    from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def pseudo_sessions(standalone_tsm_context):
    names, groups, channels = standalone_tsm_context.get_custom_instrument_names(
        "CustomInstrumentTypeId1"
    )
    for name, group, channels in zip(names, groups, channels):
        standalone_tsm_context.set_custom_session("CustomInstrumentTypeId1", name, group, channels)


@pytest.mark.pin_map("pinquerycontext.pinmap")
class TestPinQueryContext:
    @pytest.mark.usefixtures("pseudo_sessions")
    def test_get_session_and_channel_index(
        self, standalone_tsm_context: "SemiconductorModuleContext"
    ):
        (
            pin_query_context,
            session_data,
            channel_group,
            channel_list,
        ) = standalone_tsm_context.pins_to_custom_sessions(
            "CustomInstrumentTypeId1", ["DUTPin2", "DUTPin1"]
        )
        session_index, channel_index = pin_query_context.get_session_and_channel_index(1, "DUTPin1")
        assert session_index == 1
        assert channel_index == 1
