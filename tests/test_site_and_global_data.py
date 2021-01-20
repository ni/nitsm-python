import pytest

from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.mark.pin_map("site_and_global_data.pinmap")
class TestSiteAndGlobalData:
    data_id = "data_id"
    data = "2021"

    def test_set_site_data(self, standalone_tsm_context: SemiconductorModuleContext):
        standalone_tsm_context.set_site_data(self.data_id, [self.data])

    def test_get_site_data(self, standalone_tsm_context: SemiconductorModuleContext):
        queried_datas = standalone_tsm_context.get_site_data(self.data_id)
        assert isinstance(queried_datas, tuple)
        for queried_data in queried_datas:
            assert isinstance(queried_data, str)
            assert queried_data in self.data

    def test_site_data_exists(self, standalone_tsm_context: SemiconductorModuleContext):
        assert standalone_tsm_context.site_data_exists(self.data_id)

    def test_set_global_data(self, standalone_tsm_context: SemiconductorModuleContext):
        standalone_tsm_context.set_global_data(self.data_id, self.data)

    def test_get_global_data(self, standalone_tsm_context: SemiconductorModuleContext):
        queried_data = standalone_tsm_context.get_global_data(self.data_id)
        assert isinstance(queried_data, str)
        assert queried_data in self.data

    def test_global_data_exists(self, standalone_tsm_context: SemiconductorModuleContext):
        assert standalone_tsm_context.global_data_exists(self.data_id)
