# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListAdminUserStatRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.start_date: Optional[str] = None
        self.end_date: Optional[str] = None
        self.department_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.target_geo: Optional[str] = None

    @staticmethod
    def builder() -> "ListAdminUserStatRequestBuilder":
        return ListAdminUserStatRequestBuilder()


class ListAdminUserStatRequestBuilder(object):

    def __init__(self) -> None:
        list_admin_user_stat_request = ListAdminUserStatRequest()
        list_admin_user_stat_request.http_method = HttpMethod.GET
        list_admin_user_stat_request.uri = "/open-apis/admin/v1/admin_user_stats"
        list_admin_user_stat_request.token_types = {AccessTokenType.TENANT}
        self._list_admin_user_stat_request: ListAdminUserStatRequest = list_admin_user_stat_request

    def user_id_type(self, user_id_type: str) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.user_id_type = user_id_type
        self._list_admin_user_stat_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.department_id_type = department_id_type
        self._list_admin_user_stat_request.add_query("department_id_type", department_id_type)
        return self

    def start_date(self, start_date: str) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.start_date = start_date
        self._list_admin_user_stat_request.add_query("start_date", start_date)
        return self

    def end_date(self, end_date: str) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.end_date = end_date
        self._list_admin_user_stat_request.add_query("end_date", end_date)
        return self

    def department_id(self, department_id: str) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.department_id = department_id
        self._list_admin_user_stat_request.add_query("department_id", department_id)
        return self

    def user_id(self, user_id: str) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.user_id = user_id
        self._list_admin_user_stat_request.add_query("user_id", user_id)
        return self

    def page_size(self, page_size: int) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.page_size = page_size
        self._list_admin_user_stat_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.page_token = page_token
        self._list_admin_user_stat_request.add_query("page_token", page_token)
        return self

    def target_geo(self, target_geo: str) -> "ListAdminUserStatRequestBuilder":
        self._list_admin_user_stat_request.target_geo = target_geo
        self._list_admin_user_stat_request.add_query("target_geo", target_geo)
        return self

    def build(self) -> ListAdminUserStatRequest:
        return self._list_admin_user_stat_request
