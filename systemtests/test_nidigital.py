import pytest
import nidigital
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext

OPTIONS = {"Simulate": True, "driver_setup": {"Model": "6570"}}


@pytest.mark.sequence_file("nidigital.seq")
def test_nidigital(system_test_runner):
    assert system_test_runner.run()


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        session = nidigital.Session(instrument_name, options=OPTIONS)
        tsm_context.set_nidigital_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
    expected_pin_set_strings,
    expected_site_lists,
):
    # method pins_to_nidigital_session_for_ppmu
    pin_query, sessions, pin_set_strings = tsm_context.pins_to_nidigital_sessions_for_ppmu(pins)
    expected_instrument_pin_sets = set(zip(expected_instrument_names, expected_pin_set_strings))
    valid_pin_sets = []
    valid_num_pin_sets = 0

    for session, pin_set_string in zip(sessions, pin_set_strings):
        # call some methods on the session to ensure no errors
        session.ppmu_aperture_time = 0.000004
        session.ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS
        session.ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT
        session.ppmu_current_level_range = 0.000002
        session.ppmu_current_level = 0.000002
        session.ppmu_voltage_limit_high = 3.3
        session.ppmu_voltage_limit_low = 0
        session.ppmu_source()
        session.ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
        session.abort()

        # check instrument pin set we received is in the set of instrument pin sets we expected
        actual_instrument_pin_set = (session.io_resource_descriptor, pin_set_string)
        valid_pin_sets.append(actual_instrument_pin_set in expected_instrument_pin_sets)
        expected_instrument_pin_sets -= {actual_instrument_pin_set}
        valid_num_pin_sets += len(pin_set_string.split(","))

    pin_query.publish(valid_pin_sets * valid_num_pin_sets, "ValidPinSet")
    num_missing_pin_sets = [len(expected_instrument_pin_sets)] * valid_num_pin_sets
    pin_query.publish(num_missing_pin_sets, "NumMissingPinSet")

    # method pins_to_nidigital_session_for_pattern
    pin_query, sessions, site_lists = tsm_context.pins_to_nidigital_sessions_for_pattern(pins)
    expected_instrument_site_lists = set(zip(expected_instrument_names, expected_site_lists))
    valid_site_lists = []
    valid_num_site_lists = 0
    for session, site_list in zip(sessions, site_lists):
        # call some methods on the session to ensure no errors
        session.configure_active_load_levels(0.0015, -0.024, 2.0)
        session.configure_voltage_levels(0.1, 3.3, 0.5, 2.5, 5.5)
        session.commit()
        session.abort()

        # check instrument site we received is in the set of instrument sites we expected
        actual_instrument_site_list = (session.io_resource_descriptor, site_list)
        valid_site_lists.append(actual_instrument_site_list in expected_instrument_site_lists)
        expected_instrument_site_lists -= {actual_instrument_site_list}
        valid_num_site_lists += len(site_list.split(","))

    pin_query.publish(valid_site_lists * valid_num_site_lists, "ValidSite")
    num_missing_site_lists = [len(expected_instrument_site_lists)] * valid_num_site_lists
    pin_query.publish(num_missing_site_lists, "NumMissingSite")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidigital_sessions()
    for session in sessions:
        session.close()
