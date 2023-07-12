# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .delete_managers_chat_managers_request_body import DeleteManagersChatManagersRequestBody


class DeleteManagersChatManagersRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.member_id_type: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.request_body: Optional[DeleteManagersChatManagersRequestBody] = None

    @staticmethod
    def builder() -> "DeleteManagersChatManagersRequestBuilder":
        return DeleteManagersChatManagersRequestBuilder()


class DeleteManagersChatManagersRequestBuilder(object):

    def __init__(self, delete_managers_chat_managers_request: DeleteManagersChatManagersRequest = DeleteManagersChatManagersRequest()) -> None:
        delete_managers_chat_managers_request.http_method = HttpMethod.POST
        delete_managers_chat_managers_request.uri = "/open-apis/im/v1/chats/:chat_id/managers/delete_managers"
        delete_managers_chat_managers_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._delete_managers_chat_managers_request: DeleteManagersChatManagersRequest = delete_managers_chat_managers_request
    
    def member_id_type(self, member_id_type: str) -> "DeleteManagersChatManagersRequestBuilder":
        self._delete_managers_chat_managers_request.member_id_type = member_id_type
        self._delete_managers_chat_managers_request.queries["member_id_type"] = str(member_id_type)
        return self
    
    def chat_id(self, chat_id: str) -> "DeleteManagersChatManagersRequestBuilder":
        self._delete_managers_chat_managers_request.chat_id = chat_id
        self._delete_managers_chat_managers_request.paths["chat_id"] = chat_id
        return self
    
    def request_body(self, request_body: DeleteManagersChatManagersRequestBody) -> "DeleteManagersChatManagersRequestBuilder":
        self._delete_managers_chat_managers_request.request_body = request_body
        self._delete_managers_chat_managers_request.body = request_body
        return self

    def build(self) -> DeleteManagersChatManagersRequest:
        return self._delete_managers_chat_managers_request
