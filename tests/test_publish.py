import re
import random

import collections
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
    _PIN = "SystemPin1"
    _NUM_SITES = 3

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_session_for_ppmu(self._PIN)
        return pin_query_context

    def test_publish_float_scalar(self, pin_query_context, published_data_reader):
        test_data = random.random()
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == self._NUM_SITES
        for published_data_point in published_data:
            assert published_data_point.double_value == test_data

    def test_publish_bool_scalar(self, pin_query_context, published_data_reader):
        pin_query_context.publish(True)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == self._NUM_SITES
        for published_data_point in published_data:
            assert published_data_point.boolean_value


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestSinglePin1d:
    _PIN = "DUTPin1"
    _NUM_SITES = 3

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_session_for_ppmu(self._PIN)
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [random.random() for _ in range(self._NUM_SITES)]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [bool(i % 2) for i in range(self._NUM_SITES)]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_pattern(self, standalone_tsm_context, published_data_reader):
        (
            pin_query_context,
            session,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_pattern(self._PIN)
        num_sites = len(site_list.split(","))
        # alternate True and False
        test_data = collections.OrderedDict((i, bool(i % 2)) for i in range(num_sites))
        pin_query_context.publish_pattern_results(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data.values()):
            assert published_data_point.boolean_value == test_data_point


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestSinglePin2d:
    _PIN = "DUTPin3"

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu(
            self._PIN
        )
        return pin_query_context

    def test_publish_float_2d(self, pin_query_context, published_data_reader):
        # [[DigitalPattern1(ch6)], [DigitalPattern2(ch0), DigitalPattern2(ch1)]]
        test_data = [[1150.0], [1952.5, 60417]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_2d(self, pin_query_context, published_data_reader):
        # [[DigitalPattern1(ch6)], [DigitalPattern2(ch0), DigitalPattern2(ch1)]]
        test_data = [[True], [False, True]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_pattern(self, standalone_tsm_context, published_data_reader):
        (
            pin_query_context,
            sessions,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_pattern(self._PIN)
        expected_results = [True, False, True]  # test data across sites [0, 1, 2]
        pattern = re.compile(r"\s*site(\d)")
        site_lists = [
            [int(match[1]) for match in map(pattern.match, site_list.split(","))]
            for site_list in site_lists
        ]
        test_data = [  # creates data for purely jagged results [[site0], [site1, site2]]
            collections.OrderedDict((site, expected_results[site]) for site in site_list)
            for site_list in site_lists
        ]
        pin_query_context.publish_pattern_results(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(expected_results)
        for published_data_point, expected_result in zip(published_data, expected_results):
            assert published_data_point.boolean_value == expected_result


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestMultiplePins1d:
    _PINS = ["DUTPin1", "DUTPin2"]
    _NUM_SITES = 3

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_session_for_ppmu(
            self._PINS
        )
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [random.random() for _ in range(len(self._PINS) * self._NUM_SITES)]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [bool(i % 2) for i in range(len(self._PINS) * self._NUM_SITES)]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_pattern(self, standalone_tsm_context, published_data_reader):
        (
            pin_query_context,
            session,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_pattern(self._PINS)
        num_sites = len(site_list.split(","))
        # alternate True and False
        test_data = collections.OrderedDict((i, bool(i % 2)) for i in range(num_sites))
        pin_query_context.publish_pattern_results(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data.values()):
            assert published_data_point.boolean_value == test_data_point


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestMultiplePins2d:
    _PINS = ["DUTPin2", "DUTPin3"]

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu(
            self._PINS
        )
        return pin_query_context

    def test_publish_float_2d(self, pin_query_context, published_data_reader):
        # [DigitalPattern1(ch3,ch4,ch5,ch6), DigitalPattern2(ch0,ch1)]
        test_data = [[1150.0, 20.5, 30.5, -1.0], [1952.5, -60417]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_2d(self, pin_query_context, published_data_reader):
        # [DigitalPattern1(ch3,ch4,ch5,ch6), DigitalPattern2(ch0,ch1)]
        test_data = [[True, False, True, False], [True, False]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_pattern(self, standalone_tsm_context, published_data_reader):
        (
            pin_query_context,
            sessions,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_pattern(self._PINS)
        # [DigitalPattern1: site0, site1, site2], [DigitalPattern2: site1, site2]
        test_data = [{0: True, 1: False, 2: True}, {1: True, 2: True}]
        expected_results = [True, False, True]  # test_data AND'd across site
        pin_query_context.publish_pattern_results(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(expected_results)
        for published_data_point, expected_result in zip(published_data, expected_results):
            assert published_data_point.boolean_value == expected_result
