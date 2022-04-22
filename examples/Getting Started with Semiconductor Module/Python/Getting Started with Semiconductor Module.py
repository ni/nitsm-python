""" Getting Started with Semiconductor Module example!

    Example NI TSM Test Program using simulated NI-Digital and NI-DCPower instruments
"""

import random

import nidcpower
import nidigital
import nitsm.codemoduleapi
from nitsm.codemoduleapi import Capability, InstrumentTypeIdConstants
from nitsm.codemoduleapi import SemiconductorModuleContext


@nitsm.codemoduleapi.code_module
def open_dcpower_sessions(tsm_context: SemiconductorModuleContext):
    """Open NI-DCPower instrument sessions."""
    resource_strings = tsm_context.get_all_nidcpower_resource_strings()
    for resource_string in resource_strings:
        session = nidcpower.Session(
            resource_string,
            options={"Simulate": True, "DriverSetup": {"Model": "4143", "BoardType": "PXIe"}},
        )
        tsm_context.set_nidcpower_session(resource_string, session)


@nitsm.codemoduleapi.code_module
def open_digital_sessions(tsm_context: SemiconductorModuleContext):
    """Open NI-Digital instrument sessions."""
    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        session = nidigital.Session(
            instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
        )
        tsm_context.set_nidigital_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def open_all_instruments_sessions(tsm_context: SemiconductorModuleContext):
    """Open all instrument sessions."""
    open_dcpower_sessions(tsm_context)
    open_digital_sessions(tsm_context)


@nitsm.codemoduleapi.code_module
def continuity(
    tsm_context: SemiconductorModuleContext,
    pins,
):
    """Measure continuity on configured Pins (NI-DCPower, NI-Digital)."""
    dcpower_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DCPOWER, Capability.ALL
    )
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(
        dcpower_filtered_pins
    )
    per_dcpower_session_measurements = []
    dcpower_continuity_measurements = []
    for session, channel_string in zip(sessions, channel_strings):
        assert isinstance(session, nidcpower.Session)
        assert isinstance(channel_string, str)
        # call some methods on the session to ensure no errors
        pin_session = session.channels[channel_string]
        session.abort()
        pin_session.output_function = nidcpower.OutputFunction.DC_CURRENT
        pin_session.current_level = 10e-3
        pin_session.output_enabled = True
        pin_session.source_delay = 250e-6
        session.initiate()
        session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)
        per_dcpower_session_measurements = pin_session.measure_multiple()

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
        assert isinstance(session, nidigital.Session)
        assert isinstance(pin_set_string, str)

        # call some methods on the session to ensure no errors
        session.ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
        session.ppmu_voltage_level = 10e-3
        session.ppmu_source()
        per_digital_session_measurements = session.ppmu_measure(
            nidigital.PPMUMeasurementType.VOLTAGE
        )
        session.abort

        # simulate continuity data
        per_digital_session_measurements = []
        for _ in pin_set_string.split(","):
            per_dcpower_session_measurements += simulate_parametric_measurement(0.75, -0.75, 0.17)

        digital_continuity_measurements.append(per_digital_session_measurements)

    pin_query.publish(digital_continuity_measurements)


@nitsm.codemoduleapi.code_module
def leakage(
    tsm_context: SemiconductorModuleContext,
    pins,
):
    """Measure leakage on configured Pins (NI-DCPower, NI-Digital)."""
    dcpower_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DCPOWER, Capability.ALL
    )
    # Force Vcc to max=5V and measure leakage current
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(
        dcpower_filtered_pins
    )
    for session, channel_string in zip(sessions, channel_strings):
        assert isinstance(session, nidcpower.Session)
        assert isinstance(channel_string, str)
        # call some methods on the session to ensure no errors
        pin_session = session.channels[channel_string]
        session.abort()
        pin_session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        pin_session.voltage_level = 5.0
        pin_session.output_enabled = True
        pin_session.source_delay = 250e-6
        session.initiate()

    digital_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, Capability.ALL
    )
    pin_query, sessions, pin_set_strings = tsm_context.pins_to_nidigital_sessions_for_ppmu(
        digital_filtered_pins
    )

    measurements = []
    dc_max_leakage_measurements = []
    for session, pin_set_string in zip(sessions, pin_set_strings):
        assert isinstance(session, nidigital.Session)
        assert isinstance(pin_set_string, str)

        # call some methods on the session to ensure no errors
        session.ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
        session.ppmu_voltage_level = 10e-3
        session.ppmu_source()
        session.ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)
        session.abort

        # simulate leakage current
        measurements = []
        for _ in pin_set_string.split(","):
            measurements += simulate_parametric_measurement(1.05e-7, 2.2e-8, 0.19)

        dc_max_leakage_measurements.append(measurements)

    pin_query.publish(dc_max_leakage_measurements, "DC.vcc_max")

    # Turn off Vcc to 0V and measure leakage current
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(
        dcpower_filtered_pins
    )
    for session, channel_string in zip(sessions, channel_strings):
        assert isinstance(session, nidcpower.Session)
        assert isinstance(channel_string, str)
        # call some methods on the session to ensure no errors
        pin_session = session.channels[channel_string]
        session.abort()
        pin_session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        pin_session.voltage_level = 0.0
        pin_session.output_enabled = True
        pin_session.source_delay = 250e-6
        session.initiate()

    pin_query, sessions, pin_set_strings = tsm_context.pins_to_nidigital_sessions_for_ppmu(
        digital_filtered_pins
    )
    measurements = []
    dc_ground_leakage_measurements = []
    for session, pin_set_string in zip(sessions, pin_set_strings):
        assert isinstance(session, nidigital.Session)
        assert isinstance(pin_set_string, str)

        # call some methods on the session to ensure no errors
        session.ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
        session.ppmu_voltage_level = 10e-3
        session.ppmu_source()
        session.ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)
        session.abort

        # simulate leakage current
        measurements = []
        for _ in pin_set_string.split(","):
            measurements += simulate_parametric_measurement(1.05e-7, 2.2e-8, 0.19)

        dc_ground_leakage_measurements.append(measurements)

    pin_query.publish(dc_ground_leakage_measurements, "DC.gnd")


@nitsm.codemoduleapi.code_module
def functional(
    tsm_context: SemiconductorModuleContext,
    pins,
):
    """Test DUT functionality using Digital patterns."""
    filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, Capability.ALL
    )
    pin_query, sessions, site_lists = tsm_context.pins_to_nidigital_sessions_for_pattern(
        filtered_pins
    )

    # Publish pattern result expects list of dict
    pattern_results = []
    for session, site_list in zip(sessions, site_lists):
        assert isinstance(session, nidigital.Session)
        assert isinstance(site_list, str)

        # call some methods on the session to ensure no errors
        session.configure_active_load_levels(0.0015, -0.024, 2.0)
        session.configure_voltage_levels(0.1, 3.3, 0.5, 2.5, 5.5)
        session.commit()
        session.abort()

        # simulate site pass/fail data as dict with int siteNumber as key
        pattern_status = {}
        for site in site_list.split(","):
            # remove the text site and retain just the number
            site = site.replace("site", "")
            simulated_data = random.random()
            pattern_status[int(site)] = simulated_data > 0.02

        pattern_results.append(pattern_status)

    pin_query.publish_pattern_results(pattern_results)


@nitsm.codemoduleapi.code_module
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

    A random gaussian value between the limits is returned.
    """
    return ((upper_limit - lower_limit) * random.gauss(0, std_dev)) + (
        ((upper_limit - lower_limit) / 2) + lower_limit
    )
