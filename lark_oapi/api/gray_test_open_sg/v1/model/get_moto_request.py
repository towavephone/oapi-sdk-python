# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetMotoRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.body_level: Optional[str] = None
        self.moto_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetMotoRequestBuilder":
        return GetMotoRequestBuilder()


class GetMotoRequestBuilder(object):

    def __init__(self, get_moto_request: GetMotoRequest = GetMotoRequest()) -> None:
        get_moto_request.http_method = HttpMethod.GET
        get_moto_request.uri = "/open-apis/gray_test_open_sg/v1/motos/:moto_id"
        get_moto_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_moto_request: GetMotoRequest = get_moto_request
    
    def body_level(self, body_level: str) -> "GetMotoRequestBuilder":
        self._get_moto_request.body_level = body_level
        self._get_moto_request.queries["body_level"] = str(body_level)
        return self
    
    def moto_id(self, moto_id: str) -> "GetMotoRequestBuilder":
        self._get_moto_request.moto_id = moto_id
        self._get_moto_request.paths["moto_id"] = moto_id
        return self
    

    def build(self) -> GetMotoRequest:
        return self._get_moto_request
