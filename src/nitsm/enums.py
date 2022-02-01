"""Enumerations"""

import enum

__all__ = ["Capability", "InstrumentTypeIdConstants"]


class Capability(enum.Enum):
    """Differentiates between pins in the same instrument with different capabilities, such as
    NI-HSDIO Dynamic DIO channels and PFI lines.
    """

    ALL = ""
    NI_HSDIO_DYNAMIC_DIO = "NIHSDIODynamicDIOCapable"


class InstrumentTypeIdConstants(enum.Enum):
    """The type IDs for non-custom instruments in the pin map file."""

    ANY = ""
    NI_DAQMX = "niDAQmx"
    NI_DCPOWER = "niDCPower"
    NI_DIGITAL_PATTERN = "niDigitalPattern"
    NI_DMM = "niDMM"
    NI_FGEN = "niFGen"
    NI_GENERIC_MULTIPLEXER = "NIGenericMultiplexer"
    NI_HSDIO = "niHSDIO"
    NI_MODEL_BASED_INSTRUMENT = "niModelBasedInstrument"
    NI_RELAY_DRIVER = "niRelayDriver"
    NI_RFPM = "niRFPM"
    NI_RFSA = "niRFSA"
    NI_RFSG = "niRFSG"
    NI_SCOPE = "niScope"
