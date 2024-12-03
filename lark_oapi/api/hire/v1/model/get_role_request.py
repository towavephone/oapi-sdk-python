# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetRoleRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.role_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetRoleRequestBuilder":
        return GetRoleRequestBuilder()


class GetRoleRequestBuilder(object):

    def __init__(self) -> None:
        get_role_request = GetRoleRequest()
        get_role_request.http_method = HttpMethod.GET
        get_role_request.uri = "/open-apis/hire/v1/roles/:role_id"
        get_role_request.token_types = {AccessTokenType.TENANT}
        self._get_role_request: GetRoleRequest = get_role_request

    def role_id(self, role_id: str) -> "GetRoleRequestBuilder":
        self._get_role_request.role_id = role_id
        self._get_role_request.paths["role_id"] = str(role_id)
        return self

    def build(self) -> GetRoleRequest:
        return self._get_role_request
