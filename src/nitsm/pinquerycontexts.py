"""
Pin Query Contexts
"""

import itertools
import typing

__all__ = ["PinQueryContext"]

if typing.TYPE_CHECKING:
    import nitsm.pinmapinterfaces

    _PublishDataScalar = typing.Union[bool, int, float]
    _PublishDataSequence = typing.Sequence[_PublishDataScalar]
    _PublishDataJaggedSequence = typing.Sequence[_PublishDataSequence]
    _PublishDataArg = typing.Union[
        _PublishDataScalar, _PublishDataSequence, _PublishDataJaggedSequence
    ]


class PinQueryContext:
    def __init__(self, tsm_context, pins):
        self._tsm_context: nitsm.pinmapinterfaces.ISemiconductorModuleContext = tsm_context
        self._pins: typing.Union[str, typing.Sequence[str]] = pins

    def publish(self, data: "_PublishDataArg", published_data_id=""):
        """
        Publishes the measurement data for one or more pins to the Semiconductor Multi Test step
        for all sites in the PinQueryContext.

        Args:
            data: The measurement data from one or more pins connected to one or more instruments.
                The values can be bools, ints, or floats, and each value represents a measurement
                made for a single instrument channel. Pass a single value if the pin query refers
                to a single channel on a single instrument. Pass a sequence of values if the pin
                query refers to multiple channels on a single instrument or multiple instruments
                with a single channel. Pass a two dimensional sequence of values if the pin query
                refers to multiple channels on multiple instruments.
            published_data_id: The unique ID for distinguishing the measurement when you publish
                multiple measurements for the same pins within the same code module. This ID must
                match one of the values in the Published Data Id column on the Tests tab of the
                Semiconductor Multi Test step.
        """
        if isinstance(data, bool):
            return self._publish_bool_scalar(data, published_data_id)
        elif isinstance(data, (float, int)):
            return self._publish_float_scalar(data, published_data_id)
        else:
            return self._publish_sequence(data, published_data_id)

    def _publish_float_scalar(self, data, published_data_id):
        return self._publish_float_1d([data], published_data_id)

    def _publish_bool_scalar(self, data, published_data_id):
        return self._publish_bool_1d([data], published_data_id)

    def _publish_sequence(self, data, published_data_id):
        if isinstance(data[0], bool):
            return self._publish_bool_1d(data, published_data_id)
        elif isinstance(data[0], (float, int)):
            return self._publish_float_1d(data, published_data_id)
        else:
            return self._publish_sequence_2d(data, published_data_id)

    def _publish_float_1d(self, data, published_data_id):
        if isinstance(self._pins, str):
            return self._tsm_context.Publish(self._pins, published_data_id, data)
        else:
            return self._tsm_context.Publish_2(self._pins, published_data_id, data)

    def _publish_bool_1d(self, data, published_data_id):
        if isinstance(self._pins, str):
            return self._tsm_context.Publish_5(self._pins, published_data_id, data)
        else:
            return self._tsm_context.Publish_6(self._pins, published_data_id, data)

    def _publish_sequence_2d(self, data, published_data_id):
        # pad jagged sequences with 0s to make 2d sequence rectangular
        max_length = max(map(len, data))
        data = data.__class__(
            (
                sub_seq + sub_seq.__class__(itertools.repeat(0, max_length - len(sub_seq)))
                for sub_seq in data
            )
        )
        if isinstance(data[0][0], bool):
            return self._publish_bool_2d(data, published_data_id)
        else:
            return self._publish_float_2d(data, published_data_id)

    def _publish_float_2d(self, data, published_data_id):
        if isinstance(self._pins, str):
            return self._tsm_context.Publish_3(self._pins, published_data_id, data)
        else:
            return self._tsm_context.Publish_4(self._pins, published_data_id, data)

    def _publish_bool_2d(self, data, published_data_id):
        if isinstance(self._pins, str):
            return self._tsm_context.Publish_7(self._pins, published_data_id, data)
        else:
            return self._tsm_context.Publish_8(self._pins, published_data_id, data)
