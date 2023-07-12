# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class SubmitApproveNotificationRequestBody(object):
    _types = {
        "reason": str,
    }

    def __init__(self, d):
        self.reason: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SubmitApproveNotificationRequestBodyBuilder":
        return SubmitApproveNotificationRequestBodyBuilder()


class SubmitApproveNotificationRequestBodyBuilder(object):
    def __init__(self, submit_approve_notification_request_body: SubmitApproveNotificationRequestBody = SubmitApproveNotificationRequestBody({})) -> None:
        self._submit_approve_notification_request_body: SubmitApproveNotificationRequestBody = submit_approve_notification_request_body
    
    def reason(self, reason: str) -> "SubmitApproveNotificationRequestBodyBuilder":
        self._submit_approve_notification_request_body.reason = reason
        return self
    
    def build(self) -> "SubmitApproveNotificationRequestBody":
        return self._submit_approve_notification_request_body