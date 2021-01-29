import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_custom_sessions(standalone_tsm_context: SemiconductorModuleContext):
    (
        instrument_names,
        channel_group_ids,
        channel_lists,
    ) = standalone_tsm_context.get_custom_instrument_names("pytest")
    for instrument_name, channel_group_id in zip(instrument_names, channel_group_ids):
        standalone_tsm_context.set_custom_session(
            "pytest", instrument_name, channel_group_id, instrument_name
        )


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_custom_sessions")
class TestSinglePinSingleSessionQueryContext:
    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pin_to_custom_session("pytest", "SystemPin1")
        return pin_query_context

    def test_publish_float_scalar(self, pin_query_context, published_data_reader):
        pin_query_context.publish_float_scalar(1150.0)
        published_data = published_data_reader.get_and_clear_published_data()
        assert published_data.__next__().double_value == 1150.0

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [1150.0, 1952.5]
        pin_query_context.publish_float_1d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_scalar(self, pin_query_context, published_data_reader):
        test_data = True
        pin_query_context.publish_bool_scalar(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert published_data.__next__().boolean_value

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [True, False]
        pin_query_context.publish_bool_1d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_custom_sessions")
class TestSinglePinMultipleSessionQueryContext:
    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pin_to_custom_sessions("pytest", "PinGroup1")
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [1150.0, 1952.5]
        pin_query_context.publish_float_1d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_float_2d(self, pin_query_context, published_data_reader):
        test_data = [[1150.0], [1952.5]]
        pin_query_context.publish_float_2d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = (data_point for row in test_data for data_point in row)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [True, False]
        pin_query_context.publish_bool_1d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_bool_2d(self, pin_query_context, published_data_reader):
        test_data = [[True], [False]]
        pin_query_context.publish_bool_2d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = (data_point for row in test_data for data_point in row)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.boolean_value == test_data_point


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_custom_sessions")
class TestMultiplePinSingleSessionQueryContext:
    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_custom_session(
            "pytest", ["DUTPin1", "DUTPin3"]
        )
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [1150.0, 1952.5]
        pin_query_context.publish_float_1d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [True, False]
        pin_query_context.publish_bool_1d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_custom_sessions")
class TestMultiplePinMultipleSessionQueryContext:
    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_custom_sessions(
            "pytest", ["DUTPin1", "DUTPin2"]
        )
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [1150.0, 1952.5]
        pin_query_context.publish_float_1d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_float_2d(self, pin_query_context, published_data_reader):
        test_data = [[1150.0], [1952.5]]
        pin_query_context.publish_float_2d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = (data_point for row in test_data for data_point in row)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [True, False]
        pin_query_context.publish_bool_1d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_bool_2d(self, pin_query_context, published_data_reader):
        test_data = [[True], [False]]
        pin_query_context.publish_bool_2d(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = (data_point for row in test_data for data_point in row)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.boolean_value == test_data_point
