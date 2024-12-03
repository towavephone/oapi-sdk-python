# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .create_document_block_descendant_request_body import CreateDocumentBlockDescendantRequestBody


class CreateDocumentBlockDescendantRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.document_revision_id: Optional[int] = None
        self.client_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.document_id: Optional[str] = None
        self.block_id: Optional[str] = None
        self.request_body: Optional[CreateDocumentBlockDescendantRequestBody] = None

    @staticmethod
    def builder() -> "CreateDocumentBlockDescendantRequestBuilder":
        return CreateDocumentBlockDescendantRequestBuilder()


class CreateDocumentBlockDescendantRequestBuilder(object):

    def __init__(self) -> None:
        create_document_block_descendant_request = CreateDocumentBlockDescendantRequest()
        create_document_block_descendant_request.http_method = HttpMethod.POST
        create_document_block_descendant_request.uri = "/open-apis/docx/v1/documents/:document_id/blocks/:block_id/descendant"
        create_document_block_descendant_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_document_block_descendant_request: CreateDocumentBlockDescendantRequest = create_document_block_descendant_request

    def document_revision_id(self, document_revision_id: int) -> "CreateDocumentBlockDescendantRequestBuilder":
        self._create_document_block_descendant_request.document_revision_id = document_revision_id
        self._create_document_block_descendant_request.add_query("document_revision_id", document_revision_id)
        return self

    def client_token(self, client_token: str) -> "CreateDocumentBlockDescendantRequestBuilder":
        self._create_document_block_descendant_request.client_token = client_token
        self._create_document_block_descendant_request.add_query("client_token", client_token)
        return self

    def user_id_type(self, user_id_type: str) -> "CreateDocumentBlockDescendantRequestBuilder":
        self._create_document_block_descendant_request.user_id_type = user_id_type
        self._create_document_block_descendant_request.add_query("user_id_type", user_id_type)
        return self

    def document_id(self, document_id: str) -> "CreateDocumentBlockDescendantRequestBuilder":
        self._create_document_block_descendant_request.document_id = document_id
        self._create_document_block_descendant_request.paths["document_id"] = str(document_id)
        return self

    def block_id(self, block_id: str) -> "CreateDocumentBlockDescendantRequestBuilder":
        self._create_document_block_descendant_request.block_id = block_id
        self._create_document_block_descendant_request.paths["block_id"] = str(block_id)
        return self

    def request_body(self,
                     request_body: CreateDocumentBlockDescendantRequestBody) -> "CreateDocumentBlockDescendantRequestBuilder":
        self._create_document_block_descendant_request.request_body = request_body
        self._create_document_block_descendant_request.body = request_body
        return self

    def build(self) -> CreateDocumentBlockDescendantRequest:
        return self._create_document_block_descendant_request
