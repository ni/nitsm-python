import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.mark.pin_map("multi_site.pinmap")
class TestMultiSite:
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1", "SystemPin2"]
    sites = 4  # [0, 1, 2, 3]

    def test_get_semiconductor_module_with_sites(self, standalone_tsm_context):
        # Get context for sites 1 and 3
        site_numbers = [1, 3]
        filtered_tsm_context = standalone_tsm_context.get_semiconductor_module_context_with_sites(
            site_numbers
        )
        filtered_sites = list(filtered_tsm_context.site_numbers)

        # Validate the site numbers
        assert len(site_numbers) == len(filtered_sites)
        assert site_numbers == filtered_sites
        for site in site_numbers:
            assert site in filtered_sites

        # Validate that a fully initialized SemiconductorModuleContext wrapper is returned
        assert isinstance(filtered_tsm_context, SemiconductorModuleContext)
        # Exercise another wrapper method to catch initialization regressions
        pin_names = list(
            filtered_tsm_context.get_pin_names()
        )  # Should contain DUTPins and SystemPins as a tuple
        assert isinstance(pin_names, list)
        # Each item is a tuple, change it to list and compare
        assert list(pin_names[0]) == self.pin_map_dut_pins
        assert list(pin_names[1]) == self.pin_map_system_pins
