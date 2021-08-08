import pytest
from nitsm.codemoduleapi import Capability, InstrumentTypeIdConstants


@pytest.mark.pin_map("general_and_advanced.pinmap")
class TestGeneralAndAdvanced:
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]

    def test_get_pin_names(self, standalone_tsm_context):
        queried_dut_pins, queried_system_pins = standalone_tsm_context.get_pin_names(
            InstrumentTypeIdConstants.ANY, Capability.ALL
        )
        assert isinstance(queried_dut_pins, tuple)
        assert isinstance(queried_system_pins, tuple)
        assert len(queried_dut_pins) == len(self.pin_map_dut_pins)
        assert len(queried_system_pins) == len(self.pin_map_system_pins)
        for dut_pin in queried_dut_pins:
            assert isinstance(dut_pin, str)
            assert dut_pin in self.pin_map_dut_pins
        for system_pin in queried_system_pins:
            assert isinstance(system_pin, str)
            assert system_pin in self.pin_map_system_pins

    def test_filter_pins_by_instrument_type(self, standalone_tsm_context):
        filtered_pins = standalone_tsm_context.filter_pins_by_instrument_type(
            self.pin_map_dut_pins, "CustomInstrumentTypeId1", Capability.ALL
        )
        assert isinstance(filtered_pins, tuple)
        assert len(filtered_pins) == len(self.pin_map_dut_pins)
        for filtered_pin in filtered_pins:
            assert isinstance(filtered_pin, str)
            assert filtered_pin in self.pin_map_dut_pins

    @pytest.mark.parametrize("pin_groups", ("PinGroup1", ["PinGroup1"]))
    def test_get_pins_in_pin_groups(self, standalone_tsm_context, pin_groups):
        pin_group_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        queried_pins = standalone_tsm_context.get_pins_in_pin_groups(pin_groups)
        assert isinstance(queried_pins, tuple)
        assert len(queried_pins) == len(pin_group_pins)
        for queried_pin in queried_pins:
            assert isinstance(queried_pin, str)
            assert queried_pin in pin_group_pins
