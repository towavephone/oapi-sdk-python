# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetDocumentBlockChildrenRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.document_revision_id: Optional[int] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.document_id: Optional[str] = None
        self.block_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetDocumentBlockChildrenRequestBuilder":
        return GetDocumentBlockChildrenRequestBuilder()


class GetDocumentBlockChildrenRequestBuilder(object):

    def __init__(self, get_document_block_children_request: GetDocumentBlockChildrenRequest = GetDocumentBlockChildrenRequest()) -> None:
        get_document_block_children_request.http_method = HttpMethod.GET
        get_document_block_children_request.uri = "/open-apis/docx/v1/documents/:document_id/blocks/:block_id/children"
        get_document_block_children_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_document_block_children_request: GetDocumentBlockChildrenRequest = get_document_block_children_request
    
    def document_revision_id(self, document_revision_id: int) -> "GetDocumentBlockChildrenRequestBuilder":
        self._get_document_block_children_request.document_revision_id = document_revision_id
        self._get_document_block_children_request.queries["document_revision_id"] = str(document_revision_id)
        return self
    
    def page_token(self, page_token: str) -> "GetDocumentBlockChildrenRequestBuilder":
        self._get_document_block_children_request.page_token = page_token
        self._get_document_block_children_request.queries["page_token"] = str(page_token)
        return self
    
    def page_size(self, page_size: int) -> "GetDocumentBlockChildrenRequestBuilder":
        self._get_document_block_children_request.page_size = page_size
        self._get_document_block_children_request.queries["page_size"] = str(page_size)
        return self
    
    def user_id_type(self, user_id_type: str) -> "GetDocumentBlockChildrenRequestBuilder":
        self._get_document_block_children_request.user_id_type = user_id_type
        self._get_document_block_children_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def document_id(self, document_id: str) -> "GetDocumentBlockChildrenRequestBuilder":
        self._get_document_block_children_request.document_id = document_id
        self._get_document_block_children_request.paths["document_id"] = document_id
        return self
    
    def block_id(self, block_id: str) -> "GetDocumentBlockChildrenRequestBuilder":
        self._get_document_block_children_request.block_id = block_id
        self._get_document_block_children_request.paths["block_id"] = block_id
        return self
    

    def build(self) -> GetDocumentBlockChildrenRequest:
        return self._get_document_block_children_request
