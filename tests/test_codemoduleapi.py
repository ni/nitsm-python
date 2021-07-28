import pytest
from nitsm.codemoduleapi import code_module, SemiconductorModuleContext


@pytest.mark.pin_map("empty.pinmap")
class TestCodeModuleApi:
    """
    Pytest passes fixtures as keyword arguments while the code_module decorator expects the TSM
    context to be passed as a positional argument. Therefore, we must redirect the keyword argument
    to a positional argument by creating surrogate methods.
    """

    @staticmethod
    @code_module
    def _static_method(tsm_context):
        assert isinstance(tsm_context, SemiconductorModuleContext)

    def test_static_method(self, standalone_tsm_context_com_object):
        return TestCodeModuleApi._static_method(standalone_tsm_context_com_object)

    @code_module
    def _instance_method(self, tsm_context):
        assert isinstance(tsm_context, SemiconductorModuleContext)

    def test_instance_method(self, standalone_tsm_context_com_object):
        return self._instance_method(standalone_tsm_context_com_object)

    @classmethod
    @code_module
    def _class_method(cls, tsm_context):
        assert issubclass(cls, TestCodeModuleApi)
        assert isinstance(tsm_context, SemiconductorModuleContext)

    def test_class_method(self, standalone_tsm_context_com_object):
        return TestCodeModuleApi._class_method(standalone_tsm_context_com_object)

    @code_module
    def _invalid_number_of_positional_arguments(self):
        """Does not contain a positional argument for the TSM context."""
        assert False  # should not reach this point

    def test_invalid_number_of_positional_arguments(self, standalone_tsm_context_com_object):
        with pytest.raises(TypeError) as e:
            self._invalid_number_of_positional_arguments()
        assert e.value.args[0] == "Invalid number of positional arguments."
        assert e.value.args[1] == self._invalid_number_of_positional_arguments._callable

    # noinspection PyUnusedLocal
    @code_module
    def _tsm_context_not_first_positional_argument(self, something_else, tsm_context):
        assert False  # should not reach this point

    @pytest.mark.parametrize("first_argument", (None, int(), str()))
    def test_tsm_context_not_first_positional_argument(
        self, first_argument, standalone_tsm_context_com_object
    ):
        with pytest.raises(Exception) as e:
            self._tsm_context_not_first_positional_argument(
                first_argument, standalone_tsm_context_com_object
            )
        assert e.value.args[0].startswith(
            "Failed to convert Semiconductor Module context from class"
        )

    # noinspection PyUnusedLocal
    @code_module
    def _positional_arguments_after_tsm_context(self, tsm_context, *args):
        assert isinstance(tsm_context, SemiconductorModuleContext)

    def test_positional_arguments_after_tsm_context(self, standalone_tsm_context_com_object):
        self._positional_arguments_after_tsm_context(standalone_tsm_context_com_object, None)


@pytest.mark.pin_map("empty.pinmap")
def test_function(standalone_tsm_context_com_object):
    @code_module
    def func(tsm_context):
        assert isinstance(tsm_context, SemiconductorModuleContext)

    return func(standalone_tsm_context_com_object)
