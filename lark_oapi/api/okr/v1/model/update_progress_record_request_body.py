# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .content_block import ContentBlock


class UpdateProgressRecordRequestBody(object):
    _types = {
        "content": ContentBlock,
    }

    def __init__(self, d):
        self.content: Optional[ContentBlock] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateProgressRecordRequestBodyBuilder":
        return UpdateProgressRecordRequestBodyBuilder()


class UpdateProgressRecordRequestBodyBuilder(object):
    def __init__(self, update_progress_record_request_body: UpdateProgressRecordRequestBody = UpdateProgressRecordRequestBody({})) -> None:
        self._update_progress_record_request_body: UpdateProgressRecordRequestBody = update_progress_record_request_body
    
    def content(self, content: ContentBlock) -> "UpdateProgressRecordRequestBodyBuilder":
        self._update_progress_record_request_body.content = content
        return self
    
    def build(self) -> "UpdateProgressRecordRequestBody":
        return self._update_progress_record_request_body