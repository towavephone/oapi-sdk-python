# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeletePreHireRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.pre_hire_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeletePreHireRequestBuilder":
        return DeletePreHireRequestBuilder()


class DeletePreHireRequestBuilder(object):

    def __init__(self) -> None:
        delete_pre_hire_request = DeletePreHireRequest()
        delete_pre_hire_request.http_method = HttpMethod.DELETE
        delete_pre_hire_request.uri = "/open-apis/corehr/v2/pre_hires/:pre_hire_id"
        delete_pre_hire_request.token_types = {AccessTokenType.TENANT}
        self._delete_pre_hire_request: DeletePreHireRequest = delete_pre_hire_request

    def pre_hire_id(self, pre_hire_id: str) -> "DeletePreHireRequestBuilder":
        self._delete_pre_hire_request.pre_hire_id = pre_hire_id
        self._delete_pre_hire_request.paths["pre_hire_id"] = str(pre_hire_id)
        return self

    def build(self) -> DeletePreHireRequest:
        return self._delete_pre_hire_request
