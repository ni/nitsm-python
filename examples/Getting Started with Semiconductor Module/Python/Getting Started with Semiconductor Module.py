""" Getting Started with Semiconductor Module example.

    Example NI TSM Test Program using simulated NI-Digital and NI-DCPower instruments
"""

import random

import nidcpower
import nidigital
from nitsm.codemoduleapi import (
    SemiconductorModuleContext,
    code_module,
    Capability,
    InstrumentTypeIdConstants,
)


@code_module
def open_dcpower_sessions(tsm_context: SemiconductorModuleContext):
    """Open NI-DCPower instrument sessions."""
    resource_strings = tsm_context.get_all_nidcpower_resource_strings()
    for resource_string in resource_strings:
        session = nidcpower.Session(
            resource_string,
            options={"Simulate": True, "DriverSetup": {"Model": "4143", "BoardType": "PXIe"}},
        )
        tsm_context.set_nidcpower_session(resource_string, session)


@code_module
def open_digital_sessions(tsm_context: SemiconductorModuleContext):
    """Open NI-Digital instrument sessions."""
    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        session = nidigital.Session(
            instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
        )
        tsm_context.set_nidigital_session(instrument_name, session)


@code_module
def open_all_instruments_sessions(tsm_context: SemiconductorModuleContext):
    """Open all instrument sessions."""
    open_dcpower_sessions(tsm_context)
    open_digital_sessions(tsm_context)


@code_module
def continuity(
    tsm_context: SemiconductorModuleContext,
    pins,
):
    """Measure continuity on configured Pins (NI-DCPower, NI-Digital).

    This example uses simulated data and driver calls so it can run on a system without the
    NI-Digital Pattern or NI-DCPower drivers installed. Refer to the Accelerometer example
    for an example of a continuity test using the these drivers.
    """
    dcpower_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DCPOWER, Capability.ALL
    )
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(
        dcpower_filtered_pins
    )
    per_dcpower_session_measurements = []
    dcpower_continuity_measurements = []
    for session, channel_string in zip(sessions, channel_strings):
        # simulate continuity data for each channel
        per_dcpower_session_measurements = []
        for _ in channel_string.split(","):
            per_dcpower_session_measurements += simulate_parametric_measurement(0.75, -0.75, 0.17)
        dcpower_continuity_measurements.append(per_dcpower_session_measurements)

    pin_query.publish(dcpower_continuity_measurements)

    digital_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, Capability.ALL
    )
    pin_query, sessions, pin_set_strings = tsm_context.pins_to_nidigital_sessions_for_ppmu(
        digital_filtered_pins
    )
    per_digital_session_measurements = []
    digital_continuity_measurements = []
    for session, pin_set_string in zip(sessions, pin_set_strings):
        # simulate continuity data for each channel
        per_digital_session_measurements = []
        for _ in pin_set_string.split(","):
            per_dcpower_session_measurements += simulate_parametric_measurement(0.75, -0.75, 0.17)
        digital_continuity_measurements.append(per_digital_session_measurements)

    pin_query.publish(digital_continuity_measurements)


@code_module
def leakage(
    tsm_context: SemiconductorModuleContext,
    pins,
):
    """Measure leakage on configured Pins (NI-DCPower, NI-Digital).

    This example uses simulated data and driver calls so it can run on a system without the
    NI-Digital Pattern or NI-DCPower drivers installed. Refer to the Accelerometer example
    for an example of a leakage test using the these drivers.
    """
    dcpower_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DCPOWER, Capability.ALL
    )
    (
        dcpower_pin_query,
        dcpower_sessions,
        dcpower_channel_strings,
    ) = tsm_context.pins_to_nidcpower_sessions(dcpower_filtered_pins)

    digital_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, Capability.ALL
    )
    (
        digital_pin_query,
        digital_sessions,
        digital_pin_set_strings,
    ) = tsm_context.pins_to_nidigital_sessions_for_ppmu(digital_filtered_pins)

    dc_vcc_max = 5  # replace with get specification API

    # Force Vcc to max=5V and measure leakage current
    for session, channel_string in zip(dcpower_sessions, dcpower_channel_strings):
        simulate_set_power_supply_voltage(session, channel_string, dc_vcc_max)

    dc_max_leakage_measurements = []
    for session, pin_set_string in zip(digital_sessions, digital_pin_set_strings):
        # simulate leakage current
        measurements = []
        for _ in pin_set_string.split(","):
            measurements += simulate_parametric_measurement(1.05e-7, 2.2e-8, 0.19)
        dc_max_leakage_measurements.append(measurements)

    digital_pin_query.publish(dc_max_leakage_measurements, "DC.vcc_max")

    dc_gnd = 0  # replace with get specification API

    # Turn off Vcc to 0V and measure leakage current
    for session, channel_string in zip(dcpower_sessions, dcpower_channel_strings):
        simulate_set_power_supply_voltage(session, channel_string, dc_gnd)

    dc_ground_leakage_measurements = []
    for session, pin_set_string in zip(digital_sessions, digital_pin_set_strings):
        # simulate leakage current
        measurements = []
        for _ in pin_set_string.split(","):
            measurements += simulate_parametric_measurement(1.05e-7, 2.2e-8, 0.19)
        dc_ground_leakage_measurements.append(measurements)

    digital_pin_query.publish(dc_ground_leakage_measurements, "DC.gnd")


def simulate_set_power_supply_voltage(
    session: nidcpower.Session, channel_string: str, set_voltage: float
):
    """Simulate configuring a voltage on an NI-DCPower instrument."""


@code_module
def functional(
    tsm_context: SemiconductorModuleContext,
    pins,
):
    """Test DUT functionality using Digital patterns.

    This example uses simulated data and driver calls so it can run on a system without the
    NI-Digital Pattern driver installed. Refer to the Accelerometer example for an example
    of a functional test using the driver.
    """
    filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, Capability.ALL
    )
    pin_query, sessions, site_lists = tsm_context.pins_to_nidigital_sessions_for_pattern(
        filtered_pins
    )

    # Publish pattern result is a list of dict where each element corresponds to a session
    pattern_results = []
    for session, site_list in zip(sessions, site_lists):
        # simulate site pass/fail data as dict with int siteNumber as key
        pattern_status = {}
        for site in site_list.split(","):
            # remove the text site and retain just the number
            site = site.replace("site", "")
            simulated_data = random.random()
            # Simulates a functional test that bursts a pattern and gets each site failed status.
            pattern_status[int(site)] = simulated_data > 0.02

        pattern_results.append(pattern_status)

    pin_query.publish_pattern_results(pattern_results)


@code_module
def close_all_instruments_sessions(tsm_context: SemiconductorModuleContext):
    """Close all instrument sessions."""
    sessions = tsm_context.get_all_nidcpower_sessions()
    for session in sessions:
        session.close()

    sessions = tsm_context.get_all_nidigital_sessions()
    for session in sessions:
        session.close()


def simulate_parametric_measurement(upper_limit: float, lower_limit: float, std_dev: float):
    """Generate simulated parametric measurement.

    Random gaussian value between the limits is returned.
    """
    range = upper_limit - lower_limit
    return (range * random.gauss(0, std_dev)) + ((range / 2) + lower_limit)
