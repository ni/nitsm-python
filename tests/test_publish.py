import win32com.client
import pythoncom
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_custom_sessions(standalone_tsm_context: SemiconductorModuleContext):
    (
        instrument_names,
        channel_group_ids,
        channel_lists
    ) = standalone_tsm_context.get_custom_instrument_names('pytest')
    for instrument_name, channel_group_id in zip(instrument_names, channel_group_ids):
        standalone_tsm_context.set_custom_session(
            'pytest', instrument_name, channel_group_id, instrument_name
        )


@pytest.mark.pin_map('publish.pinmap')
@pytest.mark.usefixtures(
    'standalone_tsm_context', 'published_data_reader', 'simulated_custom_sessions'
)
class TestSinglePinSingleSessionQueryContext:
    def test_publish_float_scalar(self, standalone_tsm_context, published_data_reader):
        pin_query_context, *_ = standalone_tsm_context.pin_to_custom_session('pytest', 'DUTPin1')
        pin_query_context.publish_float_scalar(1150.0)
        published_data = list(published_data_reader.get_and_clear_published_data())
        assert published_data[0].double_value == 1150.0

    def test_publish_float_1d(self, standalone_tsm_context, published_data_reader):
        pin_query_context, *_ = standalone_tsm_context.pin_to_custom_session('pytest', 'DUTPin1')
        test_data = [1150.0, 1952.5]
        pin_query_context.publish_float_1d(test_data)
        published_data = list(published_data_reader.get_and_clear_published_data())
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point


    # def test_publish(self, standalone_tsm_context, published_data_reader):
    #     pin_query_context, session_data, *_ = standalone_tsm_context.pins_to_custom_sessions(
    #         'pytest', ['DUTPin1', 'DUTPin2']
    #     )
    #     test_data = list(range(len(session_data)))
    #     pin_query_context.publish_float_1d(test_data)
    #     published_data = published_data_reader.get_and_clear_published_data()
    #     for published_data_point, test_data_point in zip(published_data, test_data):
    #         assert published_data_point.double_value == test_data_point

