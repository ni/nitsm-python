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
    _PublishPatternArg = typing.Union[typing.Sequence[bool], typing.Sequence[typing.Sequence[bool]]]


def _pad_jagged_sequence(seq):
    """
    Pads a 2D jagged sequence with the default value of the element type to make it rectangular.
    The type of each sequence (tuple, list, etc) is maintained.
    """

    columns = max(map(len, seq))  # gets length of the longest row
    return type(seq)(
        (
            sub_seq + type(sub_seq)(itertools.repeat(type(sub_seq[0])(), columns - len(sub_seq)))
            for sub_seq in seq
        )
    )


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
        data = _pad_jagged_sequence(data)  # make 2d sequence rectangular
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

    def publish_pattern_results(
        self, instrument_site_pattern_results: "_PublishPatternArg", published_data_id=""
    ):
        """
        Publishes results from NI-Digital pattern burst to the Semiconductor Multi Test step for all
        sites in the Semiconductor Module context. Leave the Pin column blank for the test on the
        Semiconductor Multi Test step when publishing pattern results with this method.

        Args:
            instrument_site_pattern_results:
                The pattern result data from multiple pins connected to one or more NI-Digital
                Pattern instruments. Provide a 1D sequence to publish pattern results from a single
                NI-Digital Pattern instrument session. Provide a 2D sequence to publish pattern
                results from multiple NI-Digital Pattern instrument sessions. Each element in the
                burst results sequence(s) contains pattern results for the sites of a single
                instrument session. For multiple sessions, the size of the results sequence must be
                the same size as the session data output from the pin query method.
            published_data_id:
                The unique ID for identifying the results. This ID must match one of the values in
                the Published Data Id column on the Tests tab of the Semiconductor Multi Test step.
        """

        # convert pins to a list of pins if it isn't already
        if isinstance(self._pins, str):
            pins = [self._pins]
        else:
            pins = self._pins

        # dispatch to appropriate method based on the dimensions of the pattern results
        if isinstance(instrument_site_pattern_results[0], bool):
            return self._tsm_context.PublishPatternResults_2(
                pins, published_data_id, instrument_site_pattern_results
            )
        else:  # assumed to be 2D sequence
            instrument_site_pattern_results = _pad_jagged_sequence(instrument_site_pattern_results)
            return self._tsm_context.PublishPatternResults(
                pins, published_data_id, instrument_site_pattern_results
            )
