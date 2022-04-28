import nitsm.codemoduleapi


@nitsm.codemoduleapi.code_module
def measure(tsm_context, namespaced_symbols, expected_values):
    tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext
    if isinstance(namespaced_symbols, str):
        actual_values = tsm_context.get_specifications_value(namespaced_symbols)
    else:
        actual_values = tsm_context.get_specifications_values(namespaced_symbols)
    tsm_context.publish_per_site(expected_values == actual_values)
