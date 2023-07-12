# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class AppCustomCategory(object):
    _types = {
        "i18n_key": str,
        "description": str,
        "app_ids": List[str],
    }

    def __init__(self, d):
        self.i18n_key: Optional[str] = None
        self.description: Optional[str] = None
        self.app_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppCustomCategoryBuilder":
        return AppCustomCategoryBuilder()


class AppCustomCategoryBuilder(object):
    def __init__(self, app_custom_category: AppCustomCategory = AppCustomCategory({})) -> None:
        self._app_custom_category: AppCustomCategory = app_custom_category
    
    def i18n_key(self, i18n_key: str) -> "AppCustomCategoryBuilder":
        self._app_custom_category.i18n_key = i18n_key
        return self
    
    def description(self, description: str) -> "AppCustomCategoryBuilder":
        self._app_custom_category.description = description
        return self
    
    def app_ids(self, app_ids: List[str]) -> "AppCustomCategoryBuilder":
        self._app_custom_category.app_ids = app_ids
        return self
    
    def build(self) -> "AppCustomCategory":
        return self._app_custom_category