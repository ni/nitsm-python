import os.path
import nidigital
import pytest
from nitsm.codemoduleapi.pinquerycontexts import NIDigitalPatternSingleSessionPinQueryContext
from nitsm.codemoduleapi.pinquerycontexts import NIDigitalPatternPinQueryContext


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
    pin_map_pin_groups = ["PinGroup1"]
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

    def test_pin_to_nidigital_session(self, standalone_tsm_context, simulated_nidigital_sessions):
        (
            pin_query_context,
            queried_session,
            pin_set_string,
            site_list,
        ) = standalone_tsm_context.pin_to_nidigital_session("SystemPin1")
        assert isinstance(pin_query_context, NIDigitalPatternSingleSessionPinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        assert isinstance(site_list, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pin_to_nidigital_sessions(self, standalone_tsm_context, simulated_nidigital_sessions):
        (
            pin_query_context,
            queried_sessions,
            pin_set_strings,
            site_lists,
        ) = standalone_tsm_context.pin_to_nidigital_sessions("PinGroup1")
        assert isinstance(pin_query_context, NIDigitalPatternPinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(pin_set_strings, tuple)
        assert isinstance(site_lists, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(pin_set_strings)
        assert len(queried_sessions) == len(site_lists)
        for queried_session, pin_set_string, site_list in zip(
            queried_sessions, pin_set_strings, site_lists
        ):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(pin_set_string, str)
            assert isinstance(site_list, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session(self, standalone_tsm_context, simulated_nidigital_sessions):
        (
            pin_query_context,
            queried_session,
            pin_set_string,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session(self.pin_map_dut_pins)
        assert isinstance(pin_query_context, NIDigitalPatternSingleSessionPinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        assert isinstance(site_list, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions(self, standalone_tsm_context, simulated_nidigital_sessions):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            pin_set_strings,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions(all_pins)
        assert isinstance(pin_query_context, NIDigitalPatternPinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(pin_set_strings, tuple)
        assert isinstance(site_lists, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(pin_set_strings)
        assert len(queried_sessions) == len(site_lists)
        for queried_session, pin_set_string, site_list in zip(
            queried_sessions, pin_set_strings, site_lists
        ):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(pin_set_string, str)
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
