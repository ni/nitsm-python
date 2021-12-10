import niswitch
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext


class MockSwitchSession(niswitch.Session):
    def __init__(self, resource_name, *args, **kwargs):
        # resource name must be empty string to simulate an niswitch session
        self.__resource_name = resource_name
        super().__init__("", *args, **kwargs)

    @property
    def io_resource_descriptor(self):
        return self.__resource_name


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    module_names = tsm_context.get_relay_driver_module_names()
    for module_name in module_names:
        session = MockSwitchSession(module_name, topology="2567/Independent", simulate=True)
        tsm_context.set_relay_driver_niswitch_session(module_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    relays,
    expected_instrument_names,
    expected_relay_names,
):
    sessions, relay_names = tsm_context.relays_to_relay_driver_niswitch_sessions(relays)
    expected_instrument_relays = set(zip(expected_instrument_names, expected_relay_names))
    valid_channels = []

    for session, relay_name in zip(sessions, relay_names):
        # call some methods on the session to ensure no errors
        session.relay_control(relay_name, niswitch.RelayAction.OPEN)
        session.relay_control(relay_name, niswitch.RelayAction.CLOSE)
        session.wait_for_debounce()

        # check instrument channels we received is in the set of instrument channels we expected
        actual_instrument_relays = (session.io_resource_descriptor, relay_name)
        valid_channels.append(actual_instrument_relays in expected_instrument_relays)
        expected_instrument_relays -= {actual_instrument_relays}

    site_count = len(tsm_context.site_numbers)
    tsm_context.publish_per_site([all(valid_channels)] * site_count, "AllChannelsAreValid")
    num_missing_channels = [len(expected_instrument_relays)] * site_count
    tsm_context.publish_per_site(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_relay_driver_niswitch_sessions()
    for session in sessions:
        session.close()
