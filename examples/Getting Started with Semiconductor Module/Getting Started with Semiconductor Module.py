""" Getting Started with Semiconductor Module example.

    Example NI TSM Test Program using simulated NI-Digital and NI-DCPower instruments.
"""

import random

import nidcpower
import nidigital
import nitsm.codemoduleapi as tsm


@tsm.code_module
def add_instrument_sessions(tsm_context: tsm.SemiconductorModuleContext):
    """Open sessions for NI-Digital and NI-DCPower instruments."""
    # 1. Get the list of instruments from the pin map.
    # 2. Set the instrument driver session for each instrument (simulated here).

    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        session = nidigital.Session(
            instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
        )
        tsm_context.set_nidigital_session(instrument_name, session)

    resource_strings = tsm_context.get_all_nidcpower_resource_strings()
    for resource_string in resource_strings:
        session = nidcpower.Session(
            resource_string,
            options={"Simulate": True, "DriverSetup": {"Model": "4143", "BoardType": "PXIe"}},
        )
        tsm_context.set_nidcpower_session(resource_string, session)


@tsm.code_module
def close_instrument_sessions(tsm_context: tsm.SemiconductorModuleContext):
    """Close NI-Digital and NI-DCPower instrument sessions."""
    # 1. Get the list of instrument driver sessions.
    # 2. Close each session and cleanup resources (simulated here).
    sessions = tsm_context.get_all_nidcpower_sessions()
    for session in sessions:
        session.close()

    sessions = tsm_context.get_all_nidigital_sessions()
    for session in sessions:
        session.close()


@tsm.code_module
def continuity(
    tsm_context: tsm.SemiconductorModuleContext,
    pins,
):
    """Measure continuity on configured Pins (NI-DCPower, NI-Digital).

    This example uses simulated data and driver calls so it can run on a system without the
    NI-Digital Pattern or NI-DCPower instruments installed. Refer to the Accelerometer example
    for an example of a continuity test using the these drivers.
    """
    dcpower_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, tsm.InstrumentTypeIdConstants.NI_DCPOWER, tsm.Capability.ALL
    )
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(
        dcpower_filtered_pins
    )
    dcpower_continuity_measurements = []
    for session, channel_string in zip(sessions, channel_strings):
        # simulate continuity data for each channel
        dcpower_continuity_measurements.append(simulate_continuity_data(channel_string))

    pin_query.publish(dcpower_continuity_measurements)

    digital_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, tsm.InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, tsm.Capability.ALL
    )
    pin_query, sessions, pin_set_strings = tsm_context.pins_to_nidigital_sessions_for_ppmu(
        digital_filtered_pins
    )
    digital_continuity_measurements = []
    for session, pin_set_string in zip(sessions, pin_set_strings):
        # simulate continuity data for each channel
        digital_continuity_measurements.append(simulate_continuity_data(pin_set_string))

    pin_query.publish(digital_continuity_measurements)


@tsm.code_module
def leakage(
    tsm_context: tsm.SemiconductorModuleContext,
    pins,
):
    """Measure leakage on configured Pins (NI-DCPower, NI-Digital).

    This example uses simulated data and driver calls so it can run on a system without the
    NI-Digital Pattern or NI-DCPower instruments installed. Refer to the Accelerometer example
    for an example of a leakage test using the these drivers.
    """
    dcpower_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, tsm.InstrumentTypeIdConstants.NI_DCPOWER, tsm.Capability.ALL
    )
    (
        dcpower_pin_query,
        dcpower_sessions,
        dcpower_channel_strings,
    ) = tsm_context.pins_to_nidcpower_sessions(dcpower_filtered_pins)

    digital_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, tsm.InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, tsm.Capability.ALL
    )
    (
        digital_pin_query,
        digital_sessions,
        digital_pin_set_strings,
    ) = tsm_context.pins_to_nidigital_sessions_for_ppmu(digital_filtered_pins)

    dc_vcc_max = float(tsm_context.get_specifications_value("DC.vcc_max"))

    # Turn on power supply and force specified max value.
    for session, channel_string in zip(dcpower_sessions, dcpower_channel_strings):
        simulate_set_power_supply_voltage(session, channel_string, dc_vcc_max)

    dc_max_leakage_measurements = []
    for session, pin_set_string in zip(digital_sessions, digital_pin_set_strings):
        # simulate leakage current
        dc_max_leakage_measurements.append(simulate_leakage_data(pin_set_string))

    digital_pin_query.publish(dc_max_leakage_measurements, "DC.vcc_max")

    dc_gnd = float(tsm_context.get_specifications_value("DC.gnd"))

    # Turn off Vcc to 0V and measure leakage current
    for session, channel_string in zip(dcpower_sessions, dcpower_channel_strings):
        simulate_set_power_supply_voltage(session, channel_string, dc_gnd)

    dc_ground_leakage_measurements = []
    for session, pin_set_string in zip(digital_sessions, digital_pin_set_strings):
        # simulate leakage current
        dc_ground_leakage_measurements.append(simulate_leakage_data(pin_set_string))

    digital_pin_query.publish(dc_ground_leakage_measurements, "DC.gnd")


@tsm.code_module
def functional(
    tsm_context: tsm.SemiconductorModuleContext,
    pins,
):
    """Test DUT functionality using Digital patterns.

    This example uses simulated data and driver calls so it can run on a system without the
    NI-Digital Pattern instruments installed. Refer to the Accelerometer example for an example
    of a functional test using the driver.
    """
    filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, tsm.InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, tsm.Capability.ALL
    )
    pin_query, sessions, site_lists = tsm_context.pins_to_nidigital_sessions_for_pattern(
        filtered_pins
    )

    # Publish pattern result is a list of dict where each element corresponds to a session
    pattern_results = []
    for session, site_list in zip(sessions, site_lists):
        pattern_results.append(simulate_functional_data(site_list))

    pin_query.publish_pattern_results(pattern_results)


def simulate_set_power_supply_voltage(
    session: nidcpower.Session, channel_string: str, set_voltage: float
):
    """Simulate configuring a voltage on an NI-DCPower instrument."""
    pass


def simulate_parametric_measurement(upper_limit: float, lower_limit: float, std_dev: float):
    """Generate simulated parametric measurement.

    Random gaussian value between the limits is returned.
    """
    range = upper_limit - lower_limit
    return (range * random.gauss(0, std_dev)) + ((range / 2) + lower_limit)


def simulate_continuity_data(channel_string: str):
    """Simulate a continuity test. Generates a random data set."""
    data = []
    for _ in channel_string.split(","):
        data.append(simulate_parametric_measurement(0.75, -0.75, 0.17))
    return data


def simulate_leakage_data(channel_list: str):
    """Simulate a leakage test. Generates a random data set."""
    data = []
    for _ in channel_list.split(","):
        data.append(simulate_parametric_measurement(0.75, -0.75, 0.17))
    return data


def simulate_functional_data(site_list: str):
    """Simulate a functional test that bursts a pattern and gets each site failed status."""
    # simulate site pass/fail data as dict with int siteNumber as key
    data = {}
    for site in site_list.split(","):
        # remove the text "site" and retain just the number
        site = site.replace("site", "")
        data[int(site)] = random.random() > 0.02
    return data
