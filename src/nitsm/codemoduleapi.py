import functools
from typing import Callable as _Callable
from typing import Any as _Any
from .tsmcontext import SemiconductorModuleContext
from .enums import Capability, InstrumentTypeIdConstants

__all__ = ["SemiconductorModuleContext", "Capability", "InstrumentTypeIdConstants"]


def code_module(func):
    """
    Converts the Semiconductor Module context passed from TestStand into a native Python object. The
    Semiconductor Module context must be the first argument to the function.
    """

    @functools.wraps(func)
    def decorator(tsm_context, *args, **kwargs):
        tsm_context = SemiconductorModuleContext(tsm_context)
        return func(tsm_context, *args, **kwargs)

    return decorator
