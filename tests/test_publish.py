import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_nidigital_sessions(standalone_tsm_context: SemiconductorModuleContext):
    instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        fake_session = instrument_name
        standalone_tsm_context.set_nidigital_session(instrument_name, fake_session)


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestSinglePinScalar:

    @pytest.fixture
    def num_sites(self):
        return 2  # defined in publish.pinmap

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pin_to_nidigital_session("SystemPin1")
        return pin_query_context

    def test_publish_float_scalar(self, pin_query_context, published_data_reader, num_sites):
        pin_query_context.publish(1150.0)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == num_sites
        for published_data_point in published_data:
            assert published_data_point.double_value == 1150.0

    def test_publish_bool_scalar(self, pin_query_context, published_data_reader, num_sites):
        pin_query_context.publish(True)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == num_sites
        for published_data_point in published_data:
            assert published_data_point.boolean_value


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestSinglePin1d:
    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pin_to_nidigital_session("DUTPin1")
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [1150.0, 1952.5]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [True, False]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestSinglePin2d:
    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_sessions(["DUTPin3"])
        return pin_query_context

    def test_publish_float_2d(self, pin_query_context, published_data_reader):
        # [DigitalPattern1(ch4), DigitalPattern2(ch0)]
        test_data = [[1150.0], [1952.5]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_2d(self, pin_query_context, published_data_reader):
        # [DigitalPattern1(ch4), DigitalPattern2(ch0)]
        test_data = [[True], [False]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.boolean_value == test_data_point


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestMultiplePins1d:
    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_session(
            ["DUTPin1", "DUTPin2"]
        )
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [1150.0, 1952.5, 20.5, 33.3]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [True, False, False, True]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestMultiplePins2d:
    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_sessions(
            ["DUTPin2", "DUTPin3"]
        )
        return pin_query_context

    def test_publish_float_2d(self, pin_query_context, published_data_reader):
        # [DigitalPattern1(ch2,ch3,ch4), DigitalPattern2(ch0)]
        test_data = [[1150.0, 20.5, 30.5], [1952.5]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_2d(self, pin_query_context, published_data_reader):
        # [DigitalPattern1(ch2,ch3,ch4), DigitalPattern2(ch0)]
        test_data = [[True, False, True], [True]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.boolean_value == test_data_point
