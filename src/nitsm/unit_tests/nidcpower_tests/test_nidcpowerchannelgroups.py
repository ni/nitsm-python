from typing import Tuple, Any
import os.path
import nidcpower
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi.pinquerycontexts import *
from unit_tests.fixtures import standalone_tsm_context

T = Tuple[SemiconductorModuleContext, Any]  # enable static type checking through type alias

# Multi site pin map information
pin_map_path = os.path.join(os.path.dirname(__file__), "nidcpower_channelgroups.pinmap")
pin_map_instr_names = ["DCPower1", "DCPower2"]
pin_map_instr_channel_counts = {"DCPower1": 1, "DCPower2": 2}
pin_map_dut_pins = ["DUTPin1", "DUTPin2", "DUTPin3"]


@pytest.mark.parametrize("standalone_tsm_context", [pin_map_path], indirect=True)
def test_get_all_nidcpower_resource_strings(standalone_tsm_context: T):
    tsm, _ = standalone_tsm_context
    resource_strings = tsm.get_all_nidcpower_resource_strings()
    for resource_string in resource_strings:
        session = nidcpower.Session(resource_string, options={"Simulate": True})
        tsm.set_nidcpower_session_with_resource_string(resource_string, session)

        pin_query_context, session, channel_string = tsm.pins_to_nidcpower_session(pin_map_dut_pins)
        pass
    pass
