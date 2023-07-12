# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .draft import Draft


class UpdateDraftResponseBody(object):
    _types = {
        "draft": Draft,
    }

    def __init__(self, d):
        self.draft: Optional[Draft] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateDraftResponseBodyBuilder":
        return UpdateDraftResponseBodyBuilder()


class UpdateDraftResponseBodyBuilder(object):
    def __init__(self, update_draft_response_body: UpdateDraftResponseBody = UpdateDraftResponseBody({})) -> None:
        self._update_draft_response_body: UpdateDraftResponseBody = update_draft_response_body
    
    def draft(self, draft: Draft) -> "UpdateDraftResponseBodyBuilder":
        self._update_draft_response_body.draft = draft
        return self
    
    def build(self) -> "UpdateDraftResponseBody":
        return self._update_draft_response_body