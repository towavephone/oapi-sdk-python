# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteMessageReactionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.message_id: Optional[str] = None
        self.reaction_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteMessageReactionRequestBuilder":
        return DeleteMessageReactionRequestBuilder()


class DeleteMessageReactionRequestBuilder(object):

    def __init__(self, delete_message_reaction_request: DeleteMessageReactionRequest = DeleteMessageReactionRequest()) -> None:
        delete_message_reaction_request.http_method = HttpMethod.DELETE
        delete_message_reaction_request.uri = "/open-apis/im/v1/messages/:message_id/reactions/:reaction_id"
        delete_message_reaction_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._delete_message_reaction_request: DeleteMessageReactionRequest = delete_message_reaction_request
    
    def message_id(self, message_id: str) -> "DeleteMessageReactionRequestBuilder":
        self._delete_message_reaction_request.message_id = message_id
        self._delete_message_reaction_request.paths["message_id"] = message_id
        return self
    
    def reaction_id(self, reaction_id: str) -> "DeleteMessageReactionRequestBuilder":
        self._delete_message_reaction_request.reaction_id = reaction_id
        self._delete_message_reaction_request.paths["reaction_id"] = reaction_id
        return self
    

    def build(self) -> DeleteMessageReactionRequest:
        return self._delete_message_reaction_request
