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

    for session, site_list in zip(sessions, site_lists):
        # call some methods on the session to ensure no errors
        session.configure_active_load_levels(0.0015, -0.024, 2.0)
        session.configure_voltage_levels(0.1, 3.3, 0.5, 2.5, 5.5)
        session.commit()
        session.abort()

        # check instrument site we received is in the set of instrument sites we expected
        actual_instrument_site_list = (session.io_resource_descriptor, site_list)
        actual_in_expected = actual_instrument_site_list in expected_instrument_site_lists
        re_pattern = re.compile("\s*site(\d+)")
        site_numbers = (int(re_pattern.match(site)[1]) for site in site_list.split(","))
        valid_site_lists.append({site: actual_in_expected for site in site_numbers})
        expected_instrument_site_lists -= {actual_instrument_site_list}

    pin_query.publish_pattern_results(valid_site_lists, "ValidSiteLists")
    total_results = sum(map(len, valid_site_lists))
    num_missing_site_lists = [len(expected_instrument_site_lists)] * total_results
    pin_query.publish(num_missing_site_lists, "NumMissingSiteLists")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidigital_sessions()
    for session in sessions:
        session.close()
