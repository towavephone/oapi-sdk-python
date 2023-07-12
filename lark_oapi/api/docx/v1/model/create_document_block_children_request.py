# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .create_document_block_children_request_body import CreateDocumentBlockChildrenRequestBody


class CreateDocumentBlockChildrenRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.document_revision_id: Optional[int] = None
        self.client_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.document_id: Optional[str] = None
        self.block_id: Optional[str] = None
        self.request_body: Optional[CreateDocumentBlockChildrenRequestBody] = None

    @staticmethod
    def builder() -> "CreateDocumentBlockChildrenRequestBuilder":
        return CreateDocumentBlockChildrenRequestBuilder()


class CreateDocumentBlockChildrenRequestBuilder(object):

    def __init__(self, create_document_block_children_request: CreateDocumentBlockChildrenRequest = CreateDocumentBlockChildrenRequest()) -> None:
        create_document_block_children_request.http_method = HttpMethod.POST
        create_document_block_children_request.uri = "/open-apis/docx/v1/documents/:document_id/blocks/:block_id/children"
        create_document_block_children_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_document_block_children_request: CreateDocumentBlockChildrenRequest = create_document_block_children_request
    
    def document_revision_id(self, document_revision_id: int) -> "CreateDocumentBlockChildrenRequestBuilder":
        self._create_document_block_children_request.document_revision_id = document_revision_id
        self._create_document_block_children_request.queries["document_revision_id"] = str(document_revision_id)
        return self
    
    def client_token(self, client_token: str) -> "CreateDocumentBlockChildrenRequestBuilder":
        self._create_document_block_children_request.client_token = client_token
        self._create_document_block_children_request.queries["client_token"] = str(client_token)
        return self
    
    def user_id_type(self, user_id_type: str) -> "CreateDocumentBlockChildrenRequestBuilder":
        self._create_document_block_children_request.user_id_type = user_id_type
        self._create_document_block_children_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def document_id(self, document_id: str) -> "CreateDocumentBlockChildrenRequestBuilder":
        self._create_document_block_children_request.document_id = document_id
        self._create_document_block_children_request.paths["document_id"] = document_id
        return self
    
    def block_id(self, block_id: str) -> "CreateDocumentBlockChildrenRequestBuilder":
        self._create_document_block_children_request.block_id = block_id
        self._create_document_block_children_request.paths["block_id"] = block_id
        return self
    
    def request_body(self, request_body: CreateDocumentBlockChildrenRequestBody) -> "CreateDocumentBlockChildrenRequestBuilder":
        self._create_document_block_children_request.request_body = request_body
        self._create_document_block_children_request.body = request_body
        return self

    def build(self) -> CreateDocumentBlockChildrenRequest:
        return self._create_document_block_children_request
