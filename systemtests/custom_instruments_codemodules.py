import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext


class CustomSession:
    def __init__(self, instrument_type_id, instrument_name, channel_group_id, channel_list):
        self._instrument_type_id = instrument_type_id
        self._instrument_name = instrument_name
        self._channel_group_id = channel_group_id
        self._channel_list = channel_list

    @property
    def instrument_type_id(self):
        return self._instrument_type_id

    @property
    def instrument_name(self):
        return self._instrument_name

    @property
    def channel_group_id(self):
        return self._channel_group_id

    @property
    def channel_list(self):
        return self._channel_list


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext, instrument_type_id):
    custom_instrument_info = tsm_context.get_custom_instrument_names(instrument_type_id)
    for instrument_name, channel_group_id, channel_list in zip(*custom_instrument_info):
        session = CustomSession(instrument_type_id, instrument_name, channel_group_id, channel_list)
        tsm_context.set_custom_session(
            instrument_type_id, instrument_name, channel_group_id, session
        )


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    instrument_type_id,
    pins,
    expected_instrument_names,
    expected_channel_group_ids,
    expected_channel_lists,
):
    pin_query, *session_info = tsm_context.pins_to_custom_sessions(instrument_type_id, pins)
    expected_instrument_channels = set(
        zip(expected_instrument_names, expected_channel_group_ids, expected_channel_lists)
    )
    valid_channels = []

    for session, channel_group_id, channel_list in zip(*session_info):
        assert isinstance(session, CustomSession)
        assert session.instrument_type_id == instrument_type_id
        assert session.channel_group_id == channel_group_id

        # check instrument channels we received is in the set of instrument channels we expected
        actual_instrument_channels = (
            session.instrument_name,
            channel_group_id,
            channel_list,
        )
        channel_count = len(channel_list.split(","))
        valid_channels.append(
            [actual_instrument_channels in expected_instrument_channels] * channel_count
        )
        expected_instrument_channels -= {actual_instrument_channels}

    pin_query.publish(valid_channels)
    num_missing_channels = [
        [len(expected_instrument_channels)] * len(row) for row in valid_channels
    ]
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext, instrument_type_id):
    sessions, *_ = tsm_context.get_all_custom_sessions(instrument_type_id)
    for session in sessions:
        assert isinstance(session, CustomSession)
        assert session.instrument_type_id == instrument_type_id
