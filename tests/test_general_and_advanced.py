import pytest

from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.mark.pin_map("general_and_advanced.pinmap")
class TestGeneralAndAdvanced:
    capability = ""
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]
    pin_map_pin_group = "PinGroup1"
    pin_map_pin_groups = ["PinGroup1"]
    pin_map_instrument_type_id = "Relay1_Id"

    def test_get_pin_names(self, standalone_tsm_context: SemiconductorModuleContext):
        dut_pins, system_pins = standalone_tsm_context.get_pin_names(
            self.pin_map_instrument_type_id, self.capability
        )
        assert isinstance(dut_pins, tuple)
        assert isinstance(system_pins, tuple)
        assert len(dut_pins) == len(self.pin_map_dut_pins)
        assert len(system_pins) == len(self.pin_map_system_pins)
        for dut_pin, system_pin in zip(dut_pins, system_pins):
            assert isinstance(dut_pin, str)
            assert isinstance(system_pin, str)
            assert dut_pin in self.pin_map_dut_pins
            assert system_pin in self.pin_map_system_pins

    def test_filter_pins_by_instrument_type(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        filtered_pins = standalone_tsm_context.filter_pins_by_instrument_type(
            self.pin_map_dut_pins, self.pin_map_instrument_type_id, self.capability
        )
        assert isinstance(filtered_pins, tuple)
        assert len(filtered_pins) == len(self.pin_map_dut_pins)
        for filtered_pin in filtered_pins:
            assert isinstance(filtered_pin, str)
            assert filtered_pin in self.pin_map_dut_pins

    def test_get_pins_in_pin_group(self, standalone_tsm_context: SemiconductorModuleContext):
        pins = standalone_tsm_context.get_pins_in_pin_group(self.pin_map_pin_group)
        assert isinstance(pins, tuple)
        assert len(pins) == len(self.pin_map_dut_pins + self.pin_map_system_pins)
        for pin in pins:
            assert isinstance(pin, str)
            assert pin in self.pin_map_dut_pins + self.pin_map_system_pins

    def test_get_pins_in_pin_groups(self, standalone_tsm_context: SemiconductorModuleContext):
        pins = standalone_tsm_context.get_pins_in_pin_groups(self.pin_map_pin_groups)
        assert isinstance(pins, tuple)
        assert len(pins) == len(self.pin_map_dut_pins + self.pin_map_system_pins)
        for pin in pins:
            assert isinstance(pin, str)
            assert pin in self.pin_map_dut_pins + self.pin_map_system_pins
