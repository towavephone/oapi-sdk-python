# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ReadUsersMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.message_id: Optional[str] = None

    @staticmethod
    def builder() -> "ReadUsersMessageRequestBuilder":
        return ReadUsersMessageRequestBuilder()


class ReadUsersMessageRequestBuilder(object):

    def __init__(self, read_users_message_request: ReadUsersMessageRequest = ReadUsersMessageRequest()) -> None:
        read_users_message_request.http_method = HttpMethod.GET
        read_users_message_request.uri = "/open-apis/im/v1/messages/:message_id/read_users"
        read_users_message_request.token_types = {AccessTokenType.TENANT}
        self._read_users_message_request: ReadUsersMessageRequest = read_users_message_request
    
    def user_id_type(self, user_id_type: str) -> "ReadUsersMessageRequestBuilder":
        self._read_users_message_request.user_id_type = user_id_type
        self._read_users_message_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def page_size(self, page_size: int) -> "ReadUsersMessageRequestBuilder":
        self._read_users_message_request.page_size = page_size
        self._read_users_message_request.queries["page_size"] = str(page_size)
        return self
    
    def page_token(self, page_token: str) -> "ReadUsersMessageRequestBuilder":
        self._read_users_message_request.page_token = page_token
        self._read_users_message_request.queries["page_token"] = str(page_token)
        return self
    
    def message_id(self, message_id: str) -> "ReadUsersMessageRequestBuilder":
        self._read_users_message_request.message_id = message_id
        self._read_users_message_request.paths["message_id"] = message_id
        return self
    

    def build(self) -> ReadUsersMessageRequest:
        return self._read_users_message_request
