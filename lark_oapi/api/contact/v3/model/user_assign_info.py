# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .product_i18n_name import ProductI18nName


class UserAssignInfo(object):
    _types = {
        "subscription_id": int,
        "license_plan_key": str,
        "product_name": str,
        "i18n_name": ProductI18nName,
        "start_time": int,
        "end_time": int,
    }

    def __init__(self, d):
        self.subscription_id: Optional[int] = None
        self.license_plan_key: Optional[str] = None
        self.product_name: Optional[str] = None
        self.i18n_name: Optional[ProductI18nName] = None
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserAssignInfoBuilder":
        return UserAssignInfoBuilder()


class UserAssignInfoBuilder(object):
    def __init__(self, user_assign_info: UserAssignInfo = UserAssignInfo({})) -> None:
        self._user_assign_info: UserAssignInfo = user_assign_info
    
    def subscription_id(self, subscription_id: int) -> "UserAssignInfoBuilder":
        self._user_assign_info.subscription_id = subscription_id
        return self
    
    def license_plan_key(self, license_plan_key: str) -> "UserAssignInfoBuilder":
        self._user_assign_info.license_plan_key = license_plan_key
        return self
    
    def product_name(self, product_name: str) -> "UserAssignInfoBuilder":
        self._user_assign_info.product_name = product_name
        return self
    
    def i18n_name(self, i18n_name: ProductI18nName) -> "UserAssignInfoBuilder":
        self._user_assign_info.i18n_name = i18n_name
        return self
    
    def start_time(self, start_time: int) -> "UserAssignInfoBuilder":
        self._user_assign_info.start_time = start_time
        return self
    
    def end_time(self, end_time: int) -> "UserAssignInfoBuilder":
        self._user_assign_info.end_time = end_time
        return self
    
    def build(self) -> "UserAssignInfo":
        return self._user_assign_info