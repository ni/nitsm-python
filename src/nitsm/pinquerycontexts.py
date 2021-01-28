"""
Pin Query Contexts
"""

import typing

__all__ = [
    "NIDCPowerSinglePinSingleSessionQueryContext",
    "NIDCPowerSinglePinMultipleSessionQueryContext",
    "NIDCPowerMultiplePinSingleSessionQueryContext",
    "NIDCPowerMultiplePinMultipleSessionQueryContext",
    "NIDmmSinglePinSingleSessionQueryContext",
    "NIDmmSinglePinMultipleSessionQueryContext",
    "NIDmmMultiplePinMultipleSessionQueryContext",
    "NIFGenSinglePinSingleSessionQueryContext",
    "NIFGenSinglePinMultipleSessionQueryContext",
    "NIFGenMultiplePinSingleSessionQueryContext",
    "NIFGenMultiplePinMultipleSessionQueryContext",
    "NIScopeSinglePinSingleSessionQueryContext",
    "NIScopeSinglePinMultipleSessionQueryContext",
    "NIScopeMultiplePinSingleSessionQueryContext",
    "NIScopeMultiplePinMultipleSessionQueryContext",
    "NIDAQmxSinglePinSingleTaskQueryContext",
    "NIDAQmxSinglePinMultipleTaskQueryContext",
    "NIDAQmxMultiplePinSingleTaskQueryContext",
    "NIDAQmxMultiplePinMultipleTaskQueryContext",
    "NIDigitalPatternPinQueryContext",
    "NIDigitalPatternSingleSessionPinQueryContext",
]


if typing.TYPE_CHECKING:
    import nitsm.pinmapinterfaces


class PinQueryContext:
    def __init__(self, tsm_context: "nitsm.pinmapinterfaces.ISemiconductorModuleContext"):
        self._tsm_context = tsm_context


class SinglePinQueryContext(PinQueryContext):
    def __init__(self, tsm_context, pin):
        self.pin = pin
        super().__init__(tsm_context)


class MultiplePinQueryContext(PinQueryContext):
    def __init__(self, tsm_context, pins):
        self.pins = pins
        super().__init__(tsm_context)


class SinglePinSingleSessionQueryContext(SinglePinQueryContext):
    def publish_float_scalar(self, data, published_data_id=""):
        return self.publish_float_1d([data], published_data_id)

    def publish_float_1d(self, data, published_data_id=""):
        return self._tsm_context.Publish(self.pin, published_data_id, data)

    def publish_bool_scalar(self, data, published_data_id=""):
        return self.publish_bool_1d([data], published_data_id)

    def publish_bool_1d(self, data, published_data_id=""):
        return self._tsm_context.Publish_5(self.pin, published_data_id, data)


class SinglePinMultipleSessionQueryContext(SinglePinQueryContext):
    def publish_float_1d(self, data, published_data_id=""):
        transposed_data = [[val] for val in data]
        return self.publish_float_2d(transposed_data, published_data_id)

    def publish_float_2d(self, data, published_data_id=""):
        return self._tsm_context.Publish_3(self.pin, published_data_id, data)

    def publish_bool_1d(self, data, published_data_id=""):
        transposed_data = [[val] for val in data]
        return self.publish_bool_2d(transposed_data, published_data_id)

    def publish_bool_2d(self, data, published_data_id=""):
        return self._tsm_context.Publish_7(self.pin, published_data_id, data)


class MultiplePinSingleSessionQueryContext(MultiplePinQueryContext):
    def publish_float_1d(self, data, published_data_id=""):
        return self._tsm_context.Publish_2(self.pins, published_data_id, data)

    def publish_bool_1d(self, data, published_data_id=""):
        return self._tsm_context.Publish_6(self.pins, published_data_id, data)


class MultiplePinMultipleSessionQueryContext(MultiplePinQueryContext):
    def publish_float_1d(self, data, published_data_id=""):
        transposed_data = [[val] for val in data]
        return self.publish_float_2d(transposed_data, published_data_id)

    def publish_float_2d(self, data, published_data_id=""):
        return self._tsm_context.Publish_4(self.pins, published_data_id, data)

    def publish_bool_1d(self, data, published_data_id=""):
        transposed_data = [[val] for val in data]
        return self.publish_bool_2d(transposed_data, published_data_id)

    def publish_bool_2d(self, data, published_data_id=""):
        return self._tsm_context.Publish_8(self.pins, published_data_id, data)


class NIDCPowerSinglePinSingleSessionQueryContext(SinglePinSingleSessionQueryContext):
    pass


class NIDCPowerSinglePinMultipleSessionQueryContext(SinglePinMultipleSessionQueryContext):
    pass


class NIDCPowerMultiplePinSingleSessionQueryContext(MultiplePinSingleSessionQueryContext):
    pass


class NIDCPowerMultiplePinMultipleSessionQueryContext(MultiplePinMultipleSessionQueryContext):
    pass


class NIDmmSinglePinSingleSessionQueryContext(SinglePinSingleSessionQueryContext):
    pass


class NIDmmSinglePinMultipleSessionQueryContext(SinglePinMultipleSessionQueryContext):
    pass


class NIDmmMultiplePinMultipleSessionQueryContext(MultiplePinMultipleSessionQueryContext):
    pass


class NIFGenSinglePinSingleSessionQueryContext(SinglePinSingleSessionQueryContext):
    pass


class NIFGenSinglePinMultipleSessionQueryContext(SinglePinMultipleSessionQueryContext):
    pass


class NIFGenMultiplePinSingleSessionQueryContext(MultiplePinSingleSessionQueryContext):
    pass


class NIFGenMultiplePinMultipleSessionQueryContext(MultiplePinMultipleSessionQueryContext):
    pass


class NIScopeSinglePinSingleSessionQueryContext(SinglePinSingleSessionQueryContext):
    pass


class NIScopeSinglePinMultipleSessionQueryContext(SinglePinMultipleSessionQueryContext):
    pass


class NIScopeMultiplePinSingleSessionQueryContext(MultiplePinSingleSessionQueryContext):
    pass


class NIScopeMultiplePinMultipleSessionQueryContext(MultiplePinMultipleSessionQueryContext):
    pass


class NIDAQmxSinglePinSingleTaskQueryContext(SinglePinSingleSessionQueryContext):
    pass


class NIDAQmxSinglePinMultipleTaskQueryContext(SinglePinMultipleSessionQueryContext):
    pass


class NIDAQmxMultiplePinSingleTaskQueryContext(MultiplePinSingleSessionQueryContext):
    pass


class NIDAQmxMultiplePinMultipleTaskQueryContext(MultiplePinMultipleSessionQueryContext):
    pass


class NIDigitalPatternPinQueryContext(MultiplePinMultipleSessionQueryContext):
    pass


class NIDigitalPatternSingleSessionPinQueryContext(MultiplePinSingleSessionQueryContext):
    pass
