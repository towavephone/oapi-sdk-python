# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .form_variable_value_info_example import FormVariableValueInfoExample


class FormFieldVariableRecordValueExample(object):
    _types = {
        "country_region": FormVariableValueInfoExample,
    }

    def __init__(self, d=None):
        self.country_region: Optional[FormVariableValueInfoExample] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableRecordValueExampleBuilder":
        return FormFieldVariableRecordValueExampleBuilder()


class FormFieldVariableRecordValueExampleBuilder(object):
    def __init__(self) -> None:
        self._form_field_variable_record_value_example = FormFieldVariableRecordValueExample()

    def country_region(self,
                       country_region: FormVariableValueInfoExample) -> "FormFieldVariableRecordValueExampleBuilder":
        self._form_field_variable_record_value_example.country_region = country_region
        return self

    def build(self) -> "FormFieldVariableRecordValueExample":
        return self._form_field_variable_record_value_example
