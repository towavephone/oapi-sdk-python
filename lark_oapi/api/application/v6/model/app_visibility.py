# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .app_visible_list import AppVisibleList
from .app_visible_list import AppVisibleList


class AppVisibility(object):
    _types = {
        "is_all": bool,
        "visible_list": AppVisibleList,
        "invisible_list": AppVisibleList,
    }

    def __init__(self, d):
        self.is_all: Optional[bool] = None
        self.visible_list: Optional[AppVisibleList] = None
        self.invisible_list: Optional[AppVisibleList] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppVisibilityBuilder":
        return AppVisibilityBuilder()


class AppVisibilityBuilder(object):
    def __init__(self, app_visibility: AppVisibility = AppVisibility({})) -> None:
        self._app_visibility: AppVisibility = app_visibility
    
    def is_all(self, is_all: bool) -> "AppVisibilityBuilder":
        self._app_visibility.is_all = is_all
        return self
    
    def visible_list(self, visible_list: AppVisibleList) -> "AppVisibilityBuilder":
        self._app_visibility.visible_list = visible_list
        return self
    
    def invisible_list(self, invisible_list: AppVisibleList) -> "AppVisibilityBuilder":
        self._app_visibility.invisible_list = invisible_list
        return self
    
    def build(self) -> "AppVisibility":
        return self._app_visibility