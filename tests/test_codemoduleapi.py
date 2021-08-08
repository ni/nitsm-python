import re
import pytest
from nitsm.codemoduleapi import code_module, SemiconductorModuleContext


@pytest.mark.pin_map("codemoduleapi.pinmap")
class TestCodeModuleApi:
    @staticmethod
    @code_module
    def test_static_method_converts(standalone_tsm_context_com_object):
        assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)

    @staticmethod
    @code_module
    def test_static_method_does_not_convert(standalone_tsm_context):
        assert isinstance(standalone_tsm_context, SemiconductorModuleContext)

    @code_module
    def test_instance_method_converts(self, standalone_tsm_context_com_object):
        assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)

    @code_module
    def test_instance_method_does_not_convert(self, standalone_tsm_context):
        assert isinstance(standalone_tsm_context, SemiconductorModuleContext)

    @classmethod
    @code_module
    def test_class_method_converts(cls, standalone_tsm_context_com_object):
        assert issubclass(cls, TestCodeModuleApi)
        assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)

    @classmethod
    @code_module
    def test_class_method_does_not_convert(cls, standalone_tsm_context):
        assert issubclass(cls, TestCodeModuleApi)
        assert isinstance(standalone_tsm_context, SemiconductorModuleContext)

    @code_module
    def _invalid_number_of_positional_arguments(self):
        """Does not contain a positional argument for the TSM context."""
        assert False  # should not reach this point

    def test_invalid_number_of_positional_arguments(self):
        with pytest.raises(TypeError) as e:
            self._invalid_number_of_positional_arguments()
        assert e.value.args[0] == (
            "The number of arguments to the code module is less than expected. It must "
            "accept as it's first argument the Semiconductor Module context passed from "
            "TestStand or another code module.",
        )

    # noinspection PyUnusedLocal
    @code_module
    def _tsm_context_not_first_positional_argument(self, first_argument, tsm_context):
        assert False  # should not reach this point

    @pytest.mark.parametrize("first_argument", (None, int(), str()))
    def test_tsm_context_not_first_positional_argument(
        self, first_argument, standalone_tsm_context_com_object
    ):
        with pytest.raises(Exception) as e:
            self._tsm_context_not_first_positional_argument(
                first_argument, standalone_tsm_context_com_object
            )
        assert re.match(
            r"Failed to convert Semiconductor Module context from class '.*'\.",
            e.value.args[0],
        )

    @pytest.mark.parametrize("second_argument", (None,))
    @code_module
    def test_positional_arguments_after_tsm_context(
        self, standalone_tsm_context_com_object, second_argument
    ):
        assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)


@pytest.mark.pin_map("codemoduleapi.pinmap")
@code_module
def test_function_converts(standalone_tsm_context_com_object):
    assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)


@pytest.mark.pin_map("codemoduleapi.pinmap")
@code_module
def test_function_does_not_convert(standalone_tsm_context):
    assert isinstance(standalone_tsm_context, SemiconductorModuleContext)
