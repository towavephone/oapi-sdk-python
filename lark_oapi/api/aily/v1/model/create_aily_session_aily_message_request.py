# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .create_aily_session_aily_message_request_body import CreateAilySessionAilyMessageRequestBody


class CreateAilySessionAilyMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.aily_session_id: Optional[str] = None
        self.request_body: Optional[CreateAilySessionAilyMessageRequestBody] = None

    @staticmethod
    def builder() -> "CreateAilySessionAilyMessageRequestBuilder":
        return CreateAilySessionAilyMessageRequestBuilder()


class CreateAilySessionAilyMessageRequestBuilder(object):

    def __init__(self) -> None:
        create_aily_session_aily_message_request = CreateAilySessionAilyMessageRequest()
        create_aily_session_aily_message_request.http_method = HttpMethod.POST
        create_aily_session_aily_message_request.uri = "/open-apis/aily/v1/sessions/:aily_session_id/messages"
        create_aily_session_aily_message_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._create_aily_session_aily_message_request: CreateAilySessionAilyMessageRequest = create_aily_session_aily_message_request

    def aily_session_id(self, aily_session_id: str) -> "CreateAilySessionAilyMessageRequestBuilder":
        self._create_aily_session_aily_message_request.aily_session_id = aily_session_id
        self._create_aily_session_aily_message_request.paths["aily_session_id"] = str(aily_session_id)
        return self

    def request_body(self,
                     request_body: CreateAilySessionAilyMessageRequestBody) -> "CreateAilySessionAilyMessageRequestBuilder":
        self._create_aily_session_aily_message_request.request_body = request_body
        self._create_aily_session_aily_message_request.body = request_body
        return self

    def build(self) -> CreateAilySessionAilyMessageRequest:
        return self._create_aily_session_aily_message_request
