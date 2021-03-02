import os.path
import nidigital
import pytest
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_nidigital_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
    sessions = [
        nidigital.Session(
            instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
        )
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nidigital_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nidigital.pinmap")
class TestNIDigital:
    pin_map_instruments = ["DigitalPattern1", "DigitalPattern2"]
    pin_map_dut_pins = ["DUTPin1", "DUTPin2"]
    pin_map_system_pins = ["SystemPin1"]
    pin_map_file_path = os.path.join(os.path.dirname(__file__), "nidigital.pinmap")

    def test_get_all_nidigital_instrument_names(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_nidigital_session(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
        for instrument_name in instrument_names:
            with nidigital.Session(
                instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
            ) as session:
                standalone_tsm_context.set_nidigital_session(instrument_name, session)
                assert standalone_tsm_context._sessions[id(session)] is session

    def test_get_all_nidigital_sessions(self, standalone_tsm_context, simulated_nidigital_sessions):
        queried_sessions = standalone_tsm_context.get_all_nidigital_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidigital.Session)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session_for_ppmu_single_pin(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_session,
            pin_set_string,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_ppmu("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session_for_pattern_single_pin(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_session,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_pattern("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(site_list, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session_for_ppmu_multiple_pins(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_session,
            pin_set_string,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_ppmu(self.pin_map_dut_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session_for_pattern_multiple_pins(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_session,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_pattern(self.pin_map_dut_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(site_list, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions_for_ppmu_single_pin(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            pin_set_strings,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(pin_set_strings, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(pin_set_strings)
        for queried_session, pin_set_string in zip(queried_sessions, pin_set_strings):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(pin_set_string, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions_for_pattern_single_pin(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_pattern("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(site_lists, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(site_lists)
        for queried_session, site_list in zip(queried_sessions, site_lists):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(site_list, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions_for_ppmu_multiple_pins(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            pin_set_strings,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(pin_set_strings, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(pin_set_strings)
        for queried_session, pin_set_string in zip(queried_sessions, pin_set_strings):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(pin_set_string, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions_for_pattern_multiple_pins(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_pattern(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(site_lists, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(site_lists)
        for queried_session, site_list in zip(queried_sessions, site_lists):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(site_list, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pin_map_file_path(self, standalone_tsm_context):
        assert isinstance(standalone_tsm_context.pin_map_file_path, str)
        assert standalone_tsm_context.pin_map_file_path == self.pin_map_file_path

    # not implemented in standalone tsm and therefore can't be tested:
    # nidigital_project_specifications_file_paths
    # nidigital_project_levels_file_paths
    # nidigital_project_timing_file_paths
    # nidigital_project_pattern_file_paths
    # nidigital_project_source_waveform_file_paths
    # nidigital_project_capture_waveform_file_paths
