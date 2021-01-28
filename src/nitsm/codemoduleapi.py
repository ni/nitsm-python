import functools
from .tsmcontext import SemiconductorModuleContext
from .enums import Capability, InstrumentTypeIdConstants

__all__ = ["SemiconductorModuleContext", "Capability", "InstrumentTypeIdConstants"]


def code_module(func):
    @functools.wraps(func)
    def decorator(tsm_context, *args, **kwargs):
        tsm_context = SemiconductorModuleContext(tsm_context)
        return func(tsm_context, *args, **kwargs)

    return decorator
