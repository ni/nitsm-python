import niscope
import nitsm.codemoduleapi


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_niscope_instrument_names()
    for instrument_name in instrument_names:
        session = niscope.Session(instrument_name, options={"Simulate": True})
        tsm_context.set_niscope_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext,
    pins,
    expected_instrument_names,
    expected_channel_lists,
):
    pin_query, sessions, channel_lists = tsm_context.pins_to_niscope_sessions(pins)
    expected_instrument_channels = set(zip(expected_instrument_names, expected_channel_lists))
    valid_channels = []

    for session, channel_list in zip(sessions, channel_lists):
        # call some methods on the session to ensure no errors
        pin_session = session.channels[channel_list]
        session.abort()
        pin_session.configure_vertical(range=10.0, offset=5.0, coupling=niscope.VerticalCoupling.DC)
        session.initiate()
        pin_session.fetch_measurement_stats(niscope.ScalarMeasurement.VOLTAGE_MAX)

        # check instrument channel we received is in the set of instrument channels we expected
        actual_instrument_channel = (session.io_resource_descriptor, channel_list)
        valid_channels.append(actual_instrument_channel in expected_instrument_channels)
        expected_instrument_channels -= {actual_instrument_channel}

    pin_query.publish(valid_channels)
    num_missing_channels = [len(expected_instrument_channels)] * len(sessions)
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext):
    sessions = tsm_context.get_all_niscope_sessions()
    for session in sessions:
        session.close()
