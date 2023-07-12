# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class PatchNoteRequestBody(object):
    _types = {
        "content": str,
    }

    def __init__(self, d):
        self.content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchNoteRequestBodyBuilder":
        return PatchNoteRequestBodyBuilder()


class PatchNoteRequestBodyBuilder(object):
    def __init__(self, patch_note_request_body: PatchNoteRequestBody = PatchNoteRequestBody({})) -> None:
        self._patch_note_request_body: PatchNoteRequestBody = patch_note_request_body
    
    def content(self, content: str) -> "PatchNoteRequestBodyBuilder":
        self._patch_note_request_body.content = content
        return self
    
    def build(self) -> "PatchNoteRequestBody":
        return self._patch_note_request_body