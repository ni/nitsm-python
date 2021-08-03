import pytest


@pytest.mark.pin_map("site_and_global_data.pinmap")
class TestSiteAndGlobalData:
    site_data_id = "site_data_id"
    site_data = ["IES"]
    global_data_id = "global_data_id"
    global_data = "NI"

    @pytest.fixture
    def simulated_site_data(self, standalone_tsm_context):
        standalone_tsm_context.set_site_data(self.site_data_id, self.site_data)

    @pytest.mark.usefixtures("simulated_site_data")
    def test_get_site_data(self, standalone_tsm_context):
        queried_data = standalone_tsm_context.get_site_data(self.site_data_id)
        assert isinstance(queried_data, tuple)
        for data in queried_data:
            assert data in self.site_data

    @pytest.mark.usefixtures("simulated_site_data")
    def test_site_data_exists(self, standalone_tsm_context):
        assert standalone_tsm_context.site_data_exists(self.site_data_id)

    @pytest.mark.usefixtures("simulated_site_data")
    @pytest.mark.parametrize("delete_argument", (None, []))
    def test_delete_site_data(self, standalone_tsm_context, delete_argument):
        standalone_tsm_context.set_site_data(self.site_data_id, delete_argument)
        assert not standalone_tsm_context.site_data_exists(self.site_data_id)
        assert self.site_data_id not in standalone_tsm_context._site_data

    @pytest.fixture
    def simulated_global_data(self, standalone_tsm_context):
        standalone_tsm_context.set_global_data(self.global_data_id, self.global_data)

    @pytest.mark.usefixtures("simulated_global_data")
    def test_get_global_data(self, standalone_tsm_context):
        queried_data = standalone_tsm_context.get_global_data(self.global_data_id)
        assert queried_data == self.global_data

    @pytest.mark.usefixtures("simulated_global_data")
    def test_global_data_exists(self, standalone_tsm_context):
        assert standalone_tsm_context.global_data_exists(self.global_data_id)

    @pytest.mark.usefixtures("simulated_global_data")
    def test_delete_global_data(self, standalone_tsm_context):
        standalone_tsm_context.set_global_data(self.global_data_id, None)
        assert not standalone_tsm_context.global_data_exists(self.global_data_id)
        assert self.global_data_id not in standalone_tsm_context._global_data
