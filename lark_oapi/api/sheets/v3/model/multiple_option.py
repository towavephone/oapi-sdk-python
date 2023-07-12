# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .data_validation_value import DataValidationValue
from .option_properties import OptionProperties


class MultipleOption(object):
    _types = {
        "type": str,
        "range": str,
        "data_validation_values": List[DataValidationValue],
        "properties": OptionProperties,
    }

    def __init__(self, d):
        self.type: Optional[str] = None
        self.range: Optional[str] = None
        self.data_validation_values: Optional[List[DataValidationValue]] = None
        self.properties: Optional[OptionProperties] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MultipleOptionBuilder":
        return MultipleOptionBuilder()


class MultipleOptionBuilder(object):
    def __init__(self, multiple_option: MultipleOption = MultipleOption({})) -> None:
        self._multiple_option: MultipleOption = multiple_option
    
    def type(self, type: str) -> "MultipleOptionBuilder":
        self._multiple_option.type = type
        return self
    
    def range(self, range: str) -> "MultipleOptionBuilder":
        self._multiple_option.range = range
        return self
    
    def data_validation_values(self, data_validation_values: List[DataValidationValue]) -> "MultipleOptionBuilder":
        self._multiple_option.data_validation_values = data_validation_values
        return self
    
    def properties(self, properties: OptionProperties) -> "MultipleOptionBuilder":
        self._multiple_option.properties = properties
        return self
    
    def build(self) -> "MultipleOption":
        return self._multiple_option