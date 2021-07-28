import inspect
import functools
from .tsmcontext import SemiconductorModuleContext
from .enums import Capability, InstrumentTypeIdConstants

__all__ = ["SemiconductorModuleContext", "Capability", "InstrumentTypeIdConstants", "code_module"]


# noinspection PyPep8Naming
class code_module:
    def __init__(self, callable_):
        """
        Converts the Semiconductor Module context passed from TestStand into a native Python object.
        The Semiconductor Module context must be the first positional argument to the function or
        method.
        """

        self._callable = callable_
        functools.update_wrapper(self, callable_)

    def __get__(self, instance, owner):
        callable_ = self._callable.__get__(instance, owner)
        return self.__class__(callable_)

    def __call__(self, *args, **kwargs):
        try:
            index = int(inspect.isclass(args[0]))  # class method check
            tsm_context = args[index]
        except IndexError:
            raise TypeError("Invalid number of positional arguments.", self._callable)
        if not isinstance(tsm_context, SemiconductorModuleContext):
            try:
                tsm_context = SemiconductorModuleContext(tsm_context)
            except Exception:
                class_name = tsm_context.__class__.__name__
                raise ValueError(
                    f"Failed to convert Semiconductor Module context from class '{class_name}'."
                )
            args = *args[:index], tsm_context, *args[index + 1 :]  # noqa E203
        return self._callable(*args, **kwargs)
