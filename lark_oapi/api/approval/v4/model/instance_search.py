# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class InstanceSearch(object):
    _types = {
        "user_id": str,
        "approval_code": str,
        "instance_code": str,
        "instance_external_id": str,
        "group_external_id": str,
        "instance_title": str,
        "instance_status": str,
        "instance_start_time_from": int,
        "instance_start_time_to": int,
        "locale": str,
    }

    def __init__(self, d):
        self.user_id: Optional[str] = None
        self.approval_code: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.instance_external_id: Optional[str] = None
        self.group_external_id: Optional[str] = None
        self.instance_title: Optional[str] = None
        self.instance_status: Optional[str] = None
        self.instance_start_time_from: Optional[int] = None
        self.instance_start_time_to: Optional[int] = None
        self.locale: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceSearchBuilder":
        return InstanceSearchBuilder()


class InstanceSearchBuilder(object):
    def __init__(self, instance_search: InstanceSearch = InstanceSearch({})) -> None:
        self._instance_search: InstanceSearch = instance_search
    
    def user_id(self, user_id: str) -> "InstanceSearchBuilder":
        self._instance_search.user_id = user_id
        return self
    
    def approval_code(self, approval_code: str) -> "InstanceSearchBuilder":
        self._instance_search.approval_code = approval_code
        return self
    
    def instance_code(self, instance_code: str) -> "InstanceSearchBuilder":
        self._instance_search.instance_code = instance_code
        return self
    
    def instance_external_id(self, instance_external_id: str) -> "InstanceSearchBuilder":
        self._instance_search.instance_external_id = instance_external_id
        return self
    
    def group_external_id(self, group_external_id: str) -> "InstanceSearchBuilder":
        self._instance_search.group_external_id = group_external_id
        return self
    
    def instance_title(self, instance_title: str) -> "InstanceSearchBuilder":
        self._instance_search.instance_title = instance_title
        return self
    
    def instance_status(self, instance_status: str) -> "InstanceSearchBuilder":
        self._instance_search.instance_status = instance_status
        return self
    
    def instance_start_time_from(self, instance_start_time_from: int) -> "InstanceSearchBuilder":
        self._instance_search.instance_start_time_from = instance_start_time_from
        return self
    
    def instance_start_time_to(self, instance_start_time_to: int) -> "InstanceSearchBuilder":
        self._instance_search.instance_start_time_to = instance_start_time_to
        return self
    
    def locale(self, locale: str) -> "InstanceSearchBuilder":
        self._instance_search.locale = locale
        return self
    
    def build(self) -> "InstanceSearch":
        return self._instance_search