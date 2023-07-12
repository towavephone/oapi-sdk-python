# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .name import Name
from .name import Name
from .common_schema_config import CommonSchemaConfig


class CustomField(object):
    _types = {
        "custom_api_name": str,
        "name": Name,
        "description": Name,
        "is_open": bool,
        "is_required": bool,
        "is_unique": bool,
        "object_api_name": str,
        "type": int,
        "common_schema_config": CommonSchemaConfig,
        "create_time": str,
        "update_time": str,
    }

    def __init__(self, d):
        self.custom_api_name: Optional[str] = None
        self.name: Optional[Name] = None
        self.description: Optional[Name] = None
        self.is_open: Optional[bool] = None
        self.is_required: Optional[bool] = None
        self.is_unique: Optional[bool] = None
        self.object_api_name: Optional[str] = None
        self.type: Optional[int] = None
        self.common_schema_config: Optional[CommonSchemaConfig] = None
        self.create_time: Optional[str] = None
        self.update_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomFieldBuilder":
        return CustomFieldBuilder()


class CustomFieldBuilder(object):
    def __init__(self, custom_field: CustomField = CustomField({})) -> None:
        self._custom_field: CustomField = custom_field
    
    def custom_api_name(self, custom_api_name: str) -> "CustomFieldBuilder":
        self._custom_field.custom_api_name = custom_api_name
        return self
    
    def name(self, name: Name) -> "CustomFieldBuilder":
        self._custom_field.name = name
        return self
    
    def description(self, description: Name) -> "CustomFieldBuilder":
        self._custom_field.description = description
        return self
    
    def is_open(self, is_open: bool) -> "CustomFieldBuilder":
        self._custom_field.is_open = is_open
        return self
    
    def is_required(self, is_required: bool) -> "CustomFieldBuilder":
        self._custom_field.is_required = is_required
        return self
    
    def is_unique(self, is_unique: bool) -> "CustomFieldBuilder":
        self._custom_field.is_unique = is_unique
        return self
    
    def object_api_name(self, object_api_name: str) -> "CustomFieldBuilder":
        self._custom_field.object_api_name = object_api_name
        return self
    
    def type(self, type: int) -> "CustomFieldBuilder":
        self._custom_field.type = type
        return self
    
    def common_schema_config(self, common_schema_config: CommonSchemaConfig) -> "CustomFieldBuilder":
        self._custom_field.common_schema_config = common_schema_config
        return self
    
    def create_time(self, create_time: str) -> "CustomFieldBuilder":
        self._custom_field.create_time = create_time
        return self
    
    def update_time(self, update_time: str) -> "CustomFieldBuilder":
        self._custom_field.update_time = update_time
        return self
    
    def build(self) -> "CustomField":
        return self._custom_field