# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .follow_up import FollowUp


class PushFollowUpMessageRequestBody(object):
    _types = {
        "follow_ups": List[FollowUp],
    }

    def __init__(self, d=None):
        self.follow_ups: Optional[List[FollowUp]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PushFollowUpMessageRequestBodyBuilder":
        return PushFollowUpMessageRequestBodyBuilder()


class PushFollowUpMessageRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._push_follow_up_message_request_body = PushFollowUpMessageRequestBody()

    def follow_ups(self, follow_ups: List[FollowUp]) -> "PushFollowUpMessageRequestBodyBuilder":
        self._push_follow_up_message_request_body.follow_ups = follow_ups
        return self

    def build(self) -> "PushFollowUpMessageRequestBody":
        return self._push_follow_up_message_request_body
