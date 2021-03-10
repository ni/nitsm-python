import pytest
import nidcpower
import nidigital
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.codemoduleapi import Capability, InstrumentTypeIdConstants
import random
from random import gauss

DCPower_options = {"Simulate": True, "DriverSetup": {"Model": "4141", "BoardType": "PXIe"}}
Digital_options = {"Simulate": True, "driver_setup": {"Model": "6570"}}


@pytest.mark.sequence_file("Getting Started with Semiconductor Module.seq")
def test_getting_started_with_semiconductor_module(system_test_runner):
    assert system_test_runner.run()


@nitsm.codemoduleapi.code_module
def open_dcpower_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names, channel_strings = tsm_context.get_all_nidcpower_instrument_names()
    for instrument_name, channel_string in zip(instrument_names, channel_strings):
        session = nidcpower.Session(instrument_name, channel_string, options=DCPower_options)
        tsm_context.set_nidcpower_session_with_channel_string(
            instrument_name, channel_string, session
        )


@nitsm.codemoduleapi.code_module
def open_digital_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        session = nidigital.Session(instrument_name, options=Digital_options)
        tsm_context.set_nidigital_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def continuity(
    tsm_context: SemiconductorModuleContext,
    pins,
):
    dcpower_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DCPOWER, Capability.ALL
    )
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(
        dcpower_filtered_pins
    )
    measurements = ()
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
        pin_session.measure(nidcpower.MeasurementTypes.VOLTAGE)
        # simulate continuity data
        measurements += ((((0.75 - -0.75) * gauss(0, 0.17)) + (((0.75 - -0.75) / 2) + -0.75)),)
        dcpower_continuity_measurements.append(measurements)

    pin_query.publish(dcpower_continuity_measurements)

    digital_filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, Capability.ALL
    )
    pin_query, sessions, pin_set_strings = tsm_context.pins_to_nidigital_sessions_for_ppmu(
        digital_filtered_pins
    )
    measurements = ()
    digital_continuity_measurements = []
    for session, pin_set_string in zip(sessions, pin_set_strings):
        assert isinstance(session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        for _ in pin_set_string.split(","):
            # call some methods on the session to ensure no errors
            session.ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
            session.ppmu_voltage_level = 10e-3
            session.ppmu_source()
            session.ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)
            session.abort
            # simulate continuity data
            measurements += ((((0.75 - -0.75) * gauss(0, 0.17)) + (((0.75 - -0.75) / 2) + -0.75)),)
        digital_continuity_measurements.append(measurements)

    pin_query.publish(digital_continuity_measurements)


@nitsm.codemoduleapi.code_module
def leakage(
    tsm_context: SemiconductorModuleContext,
    pins,
):

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
    measurements = ()
    DC_max_leakage_measurements = []
    for session, pin_set_string in zip(sessions, pin_set_strings):
        assert isinstance(session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        for _ in pin_set_string.split(","):
            # call some methods on the session to ensure no errors
            session.ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
            session.ppmu_voltage_level = 10e-3
            session.ppmu_source()
            session.ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)
            session.abort
            # simulate leakage current using a 50µA range
            measurements += (
                (((1.05e-7 - 2.2e-8) * gauss(0, 0.19)) + (((1.05e-7 - 2.2e-8) / 2) + 2.2e-8)),
            )
        DC_max_leakage_measurements.append(measurements)

    pin_query.publish(DC_max_leakage_measurements, "DC.vcc_max")

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
    measurements = ()
    DC_ground_leakage_measurements = []
    for session, pin_set_string in zip(sessions, pin_set_strings):
        assert isinstance(session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        for _ in pin_set_string.split(","):
            # call some methods on the session to ensure no errors
            session.ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
            session.ppmu_voltage_level = 10e-3
            session.ppmu_source()
            session.ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)
            session.abort
            # simulate leakage current using a 50µA range
            measurements += (
                (((1.05e-7 - 2.2e-8) * gauss(0, 0.19)) + (((1.05e-7 - 2.2e-8) / 2) + 2.2e-8)),
            )
        DC_ground_leakage_measurements.append(measurements)

    pin_query.publish(DC_ground_leakage_measurements, "DC.gnd")


@nitsm.codemoduleapi.code_module
def functional(
    tsm_context: SemiconductorModuleContext,
    pins,
):
    filtered_pins = tsm_context.filter_pins_by_instrument_type(
        pins, InstrumentTypeIdConstants.NI_DIGITAL_PATTERN, Capability.ALL
    )
    pin_query, sessions, site_lists = tsm_context.pins_to_nidigital_sessions_for_pattern(
        filtered_pins
    )
    pattern_status = ()
    pattern_results = []
    for session, site_list in zip(sessions, site_lists):
        assert isinstance(session, nidigital.Session)
        assert isinstance(site_list, str)
        for _ in site_list.split(","):
            # call some methods on the session to ensure no errors
            session.configure_active_load_levels(0.0015, -0.024, 2.0)
            session.configure_voltage_levels(0.1, 3.3, 0.5, 2.5, 5.5)
            session.commit()
            session.abort()
            # simulate functional data and pattern status
            simulated_data = random.random()
            pattern_status += (simulated_data > 0.02,)
        pattern_results.append(pattern_status)

    pin_query.publish_pattern_result(pattern_results)


@nitsm.codemoduleapi.code_module
def close_all_instruments_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidcpower_sessions()
    for session in sessions:
        session.close()

    sessions = tsm_context.get_all_nidigital_sessions()
    for session in sessions:
        session.close()
