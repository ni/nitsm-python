import functools
from .tsmcontext import SemiconductorModuleContext
from .enums import Capability, InstrumentTypeIdConstants

__all__ = ["SemiconductorModuleContext", "Capability", "InstrumentTypeIdConstants"]


def code_module(callable_):
    """
    Converts the Semiconductor Module context passed from TestStand into a native Python object. The
    Semiconductor Module context must be the first argument to the function.
    """

    @functools.wraps(callable_)
    def nitsm_code_module(tsm_context, *args, **kwargs):
        if not isinstance(tsm_context, SemiconductorModuleContext):
            tsm_context = SemiconductorModuleContext(tsm_context)
        return callable_(tsm_context, *args, **kwargs)

    return nitsm_code_module
