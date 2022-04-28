import nitsm.codemoduleapi as tsm

MULTIPLEXER_TYPE_ID = "SimulatedMultiplexer"


@tsm.code_module
def open_sessions(tsm_context: tsm.SemiconductorModuleContext):
    switch_names = tsm_context.get_all_switch_names(MULTIPLEXER_TYPE_ID)
    for switch_name in switch_names:
        tsm_context.set_switch_session(switch_name, switch_name, MULTIPLEXER_TYPE_ID)
    # nidigital sessions are required to satisfy the pin map but won't be used
    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        tsm_context.set_nidigital_session(instrument_name, ...)


@tsm.code_module
def measure(
    tsm_context: tsm.SemiconductorModuleContext, pin, expected_switch_names, expected_switch_routes
):
    site_contexts, switch_names, switch_routes = tsm_context.pin_to_switch_sessions(
        pin, MULTIPLEXER_TYPE_ID
    )
    expected_names_and_routes = set(zip(expected_switch_names, expected_switch_routes))
    valid_names_and_routes = []

    for site_context, switch_name, switch_route in zip(site_contexts, switch_names, switch_routes):
        # check switch route we received is in the set of switch routes we expected
        actual_name_and_route = (switch_name, switch_route)
        valid_name_and_route = actual_name_and_route in expected_names_and_routes
        valid_names_and_routes.append(valid_name_and_route)
        expected_names_and_routes.discard(actual_name_and_route)
        # get a pin query context and publish result
        pin_query = site_context.pins_to_nidigital_session_for_ppmu(pin)[0]
        pin_query.publish(valid_name_and_route)

    # publish missing switch routes for all sites
    pin_query = tsm_context.pins_to_nidigital_session_for_ppmu(pin)[0]
    num_missing_routes = [len(expected_names_and_routes)] * len(site_contexts)
    pin_query.publish(num_missing_routes, "NumMissing")


@tsm.code_module
def close_sessions(tsm_context: tsm.SemiconductorModuleContext):
    tsm_context.get_all_switch_sessions(MULTIPLEXER_TYPE_ID)
