# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .extract_entity_request_body import ExtractEntityRequestBody


class ExtractEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ExtractEntityRequestBody] = None

    @staticmethod
    def builder() -> "ExtractEntityRequestBuilder":
        return ExtractEntityRequestBuilder()


class ExtractEntityRequestBuilder(object):

    def __init__(self, extract_entity_request: ExtractEntityRequest = ExtractEntityRequest()) -> None:
        extract_entity_request.http_method = HttpMethod.POST
        extract_entity_request.uri = "/open-apis/baike/v1/entities/extract"
        extract_entity_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._extract_entity_request: ExtractEntityRequest = extract_entity_request
    
    def request_body(self, request_body: ExtractEntityRequestBody) -> "ExtractEntityRequestBuilder":
        self._extract_entity_request.request_body = request_body
        self._extract_entity_request.body = request_body
        return self

    def build(self) -> ExtractEntityRequest:
        return self._extract_entity_request
