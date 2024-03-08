# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.provider: Optional[str] = None
        self.outer_id: Optional[str] = None
        self.entity_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteEntityRequestBuilder":
        return DeleteEntityRequestBuilder()


class DeleteEntityRequestBuilder(object):

    def __init__(self) -> None:
        delete_entity_request = DeleteEntityRequest()
        delete_entity_request.http_method = HttpMethod.DELETE
        delete_entity_request.uri = "/open-apis/lingo/v1/entities/:entity_id"
        delete_entity_request.token_types = {AccessTokenType.TENANT}
        self._delete_entity_request: DeleteEntityRequest = delete_entity_request

    def provider(self, provider: str) -> "DeleteEntityRequestBuilder":
        self._delete_entity_request.provider = provider
        self._delete_entity_request.add_query("provider", provider)
        return self

    def outer_id(self, outer_id: str) -> "DeleteEntityRequestBuilder":
        self._delete_entity_request.outer_id = outer_id
        self._delete_entity_request.add_query("outer_id", outer_id)
        return self

    def entity_id(self, entity_id: str) -> "DeleteEntityRequestBuilder":
        self._delete_entity_request.entity_id = entity_id
        self._delete_entity_request.paths["entity_id"] = str(entity_id)
        return self

    def build(self) -> DeleteEntityRequest:
        return self._delete_entity_request
