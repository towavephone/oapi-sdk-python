# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .highlight_entity_request_body import HighlightEntityRequestBody


class HighlightEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[HighlightEntityRequestBody] = None

    @staticmethod
    def builder() -> "HighlightEntityRequestBuilder":
        return HighlightEntityRequestBuilder()


class HighlightEntityRequestBuilder(object):

    def __init__(self, highlight_entity_request: HighlightEntityRequest = HighlightEntityRequest()) -> None:
        highlight_entity_request.http_method = HttpMethod.POST
        highlight_entity_request.uri = "/open-apis/baike/v1/entities/highlight"
        highlight_entity_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._highlight_entity_request: HighlightEntityRequest = highlight_entity_request
    
    def request_body(self, request_body: HighlightEntityRequestBody) -> "HighlightEntityRequestBuilder":
        self._highlight_entity_request.request_body = request_body
        self._highlight_entity_request.body = request_body
        return self

    def build(self) -> HighlightEntityRequest:
        return self._highlight_entity_request
