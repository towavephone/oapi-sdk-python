# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .create_document_request_body import CreateDocumentRequestBody


class CreateDocumentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateDocumentRequestBody] = None

    @staticmethod
    def builder() -> "CreateDocumentRequestBuilder":
        return CreateDocumentRequestBuilder()


class CreateDocumentRequestBuilder(object):

    def __init__(self, create_document_request: CreateDocumentRequest = CreateDocumentRequest()) -> None:
        create_document_request.http_method = HttpMethod.POST
        create_document_request.uri = "/open-apis/docx/v1/documents"
        create_document_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_document_request: CreateDocumentRequest = create_document_request
    
    def request_body(self, request_body: CreateDocumentRequestBody) -> "CreateDocumentRequestBuilder":
        self._create_document_request.request_body = request_body
        self._create_document_request.body = request_body
        return self

    def build(self) -> CreateDocumentRequest:
        return self._create_document_request
