# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .note import Note


class CreateNoteRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[Note] = None

    @staticmethod
    def builder() -> "CreateNoteRequestBuilder":
        return CreateNoteRequestBuilder()


class CreateNoteRequestBuilder(object):

    def __init__(self, create_note_request: CreateNoteRequest = CreateNoteRequest()) -> None:
        create_note_request.http_method = HttpMethod.POST
        create_note_request.uri = "/open-apis/hire/v1/notes"
        create_note_request.token_types = {AccessTokenType.TENANT}
        self._create_note_request: CreateNoteRequest = create_note_request
    
    def user_id_type(self, user_id_type: str) -> "CreateNoteRequestBuilder":
        self._create_note_request.user_id_type = user_id_type
        self._create_note_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def request_body(self, request_body: Note) -> "CreateNoteRequestBuilder":
        self._create_note_request.request_body = request_body
        self._create_note_request.body = request_body
        return self

    def build(self) -> CreateNoteRequest:
        return self._create_note_request
