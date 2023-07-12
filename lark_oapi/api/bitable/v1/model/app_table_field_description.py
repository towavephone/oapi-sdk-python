# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class AppTableFieldDescription(object):
    _types = {
        "disable_sync": bool,
        "text": str,
    }

    def __init__(self, d):
        self.disable_sync: Optional[bool] = None
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableFieldDescriptionBuilder":
        return AppTableFieldDescriptionBuilder()


class AppTableFieldDescriptionBuilder(object):
    def __init__(self, app_table_field_description: AppTableFieldDescription = AppTableFieldDescription({})) -> None:
        self._app_table_field_description: AppTableFieldDescription = app_table_field_description
    
    def disable_sync(self, disable_sync: bool) -> "AppTableFieldDescriptionBuilder":
        self._app_table_field_description.disable_sync = disable_sync
        return self
    
    def text(self, text: str) -> "AppTableFieldDescriptionBuilder":
        self._app_table_field_description.text = text
        return self
    
    def build(self) -> "AppTableFieldDescription":
        return self._app_table_field_description