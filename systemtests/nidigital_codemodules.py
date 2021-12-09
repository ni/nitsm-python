import re
import nidigital
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext

OPTIONS = {"Simulate": True, "driver_setup": {"Model": "6570"}}


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        session = nidigital.Session(instrument_name, options=OPTIONS)
        session.load_pin_map(tsm_context.pin_map_file_path)
        session.load_specifications_levels_and_timing(
            tsm_context.nidigital_project_specifications_file_paths,
            tsm_context.nidigital_project_levels_file_paths,
            tsm_context.nidigital_project_timing_file_paths,
        )
        session.apply_levels_and_timing("nidigital", "nidigital")
        for pattern_file_path in tsm_context.nidigital_project_pattern_file_paths:
            session.load_pattern(pattern_file_path)
        tsm_context.set_nidigital_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure_ppmu(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
    expected_pin_set_strings,
):
    pin_query, sessions, pin_set_strings = tsm_context.pins_to_nidigital_sessions_for_ppmu(pins)
    expected_instrument_pin_sets = set(zip(expected_instrument_names, expected_pin_set_strings))
    valid_pin_sets = []

    for session, pin_set_string in zip(sessions, pin_set_strings):
        # call some methods on the session to ensure no errors
        session.pins[pin_set_string].ppmu_aperture_time = 4e-6
        session.pins[
            pin_set_string
        ].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS
        session.pins[pin_set_string].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT
        session.pins[pin_set_string].ppmu_current_level_range = 2e-6
        session.pins[pin_set_string].ppmu_current_level = 2e-6
        session.pins[pin_set_string].ppmu_voltage_limit_high = 3.3
        session.pins[pin_set_string].ppmu_voltage_limit_low = 0
        session.pins[pin_set_string].ppmu_source()
        session.pins[pin_set_string].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
        session.abort()

        # check instrument pin set we received is in the set of instrument pin sets we expected
        actual_instrument_pin_set = (session.io_resource_descriptor, pin_set_string)
        num_pins_for_session = len(pin_set_string.split(","))
        valid_pin_sets.extend(
            [actual_instrument_pin_set in expected_instrument_pin_sets] * num_pins_for_session
        )
        expected_instrument_pin_sets -= {actual_instrument_pin_set}

    pin_query.publish(valid_pin_sets, "ValidPinSetStrings")
    num_missing_pin_sets = [len(expected_instrument_pin_sets)] * len(valid_pin_sets)
    pin_query.publish(num_missing_pin_sets, "NumMissingPinSetStrings")


@nitsm.codemoduleapi.code_module
def measure_pattern(
    tsm_context: SemiconductorModuleContext, pins, expected_instrument_names, expected_site_lists
):
    pin_query, sessions, site_lists = tsm_context.pins_to_nidigital_sessions_for_pattern(pins)
    expected_instrument_site_lists = set(zip(expected_instrument_names, expected_site_lists))
    valid_site_lists = []
    re_pattern = re.compile(r"\s*site(\d+)")

    for session, site_list in zip(sessions, site_lists):
        # call some methods on the session to ensure no errors
        session.sites[site_list].burst_pattern("start_label")

        # check instrument site we received is in the set of instrument sites we expected
        actual_instrument_site_list = (session.io_resource_descriptor, site_list)
        actual_in_expected = actual_instrument_site_list in expected_instrument_site_lists
        site_numbers = (int(re_pattern.match(site)[1]) for site in site_list.split(","))
        valid_site_lists.append({site: actual_in_expected for site in site_numbers})
        expected_instrument_site_lists -= {actual_instrument_site_list}

    pin_query.publish_pattern_results(valid_site_lists, "ValidSiteLists")
    num_missing_site_lists = [len(expected_instrument_site_lists)] * len(tsm_context.site_numbers)
    tsm_context.publish_per_site(num_missing_site_lists, "NumMissingSiteLists")


@nitsm.codemoduleapi.code_module
def check_project_paths(
    tsm_context: SemiconductorModuleContext,
    specifications_paths,
    levels_paths,
    timing_paths,
    pattern_paths,
    source_waveform_paths,
    capture_waveform_paths,
):
    site_count = len(tsm_context.site_numbers)
    valid_project_paths = [
        tsm_context.nidigital_project_specifications_file_paths == tuple(specifications_paths)
    ] * site_count
    valid_levels_paths = [
        tsm_context.nidigital_project_levels_file_paths == tuple(levels_paths)
    ] * site_count
    valid_timing_paths = [
        tsm_context.nidigital_project_timing_file_paths == tuple(timing_paths)
    ] * site_count
    valid_pattern_paths = [
        tsm_context.nidigital_project_pattern_file_paths == tuple(pattern_paths)
    ] * site_count
    valid_source_waveform_paths = [
        tsm_context.nidigital_project_source_waveform_file_paths == tuple(source_waveform_paths)
    ] * site_count
    valid_capture_waveform_paths = [
        tsm_context.nidigital_project_capture_waveform_file_paths == tuple(capture_waveform_paths)
    ] * site_count

    tsm_context.publish_per_site(valid_project_paths, "ValidSpecificationsPaths")
    tsm_context.publish_per_site(valid_levels_paths, "ValidLevelsPaths")
    tsm_context.publish_per_site(valid_timing_paths, "ValidTimingPaths")
    tsm_context.publish_per_site(valid_pattern_paths, "ValidPatternPaths")
    tsm_context.publish_per_site(valid_source_waveform_paths, "ValidSourceWaveformPaths")
    tsm_context.publish_per_site(valid_capture_waveform_paths, "ValidCaptureWaveformPaths")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidigital_sessions()
    for session in sessions:
        session.close()
