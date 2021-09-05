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
        The Semiconductor Module context must be the first argument to the function or method.
        """

        self._callable = callable_
        self._signature = inspect.signature(callable_)
        functools.update_wrapper(self, callable_)

    def __get__(self, instance, owner):
        callable_ = self._callable.__get__(instance, owner)
        return self.__class__(callable_)

    def __call__(self, *args, **kwargs):
        bound_arguments = self._signature.bind(*args, **kwargs)
        arguments_iter = iter(bound_arguments.arguments.items())

        # find potential argument that could be the tsm context
        try:
            argument = next(arguments_iter)  # get first argument
            if inspect.isclass(argument[1]):  # class method check
                argument = next(arguments_iter)  # move to second argument
        except StopIteration:
            raise TypeError(
                (
                    "The number of arguments to the code module is less than expected. It must "
                    "accept as it's first argument the Semiconductor Module context passed from "
                    "TestStand or another code module.",
                )
            )

        # attempt to wrap argument in a SemiconductorModuleContext class
        argument_name, argument_value = argument
        if not isinstance(argument_value, SemiconductorModuleContext):
            try:
                argument_value = SemiconductorModuleContext(argument_value)
            except Exception:
                class_name = argument_value.__class__.__name__
                raise ValueError(
                    f"Failed to convert Semiconductor Module context from class '{class_name}'.",
                )
            bound_arguments.arguments[argument_name] = argument_value

        return self._callable(*bound_arguments.args, **bound_arguments.kwargs)
