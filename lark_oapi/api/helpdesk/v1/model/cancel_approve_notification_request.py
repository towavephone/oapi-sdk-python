# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class CancelApproveNotificationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.notification_id: Optional[str] = None

    @staticmethod
    def builder() -> "CancelApproveNotificationRequestBuilder":
        return CancelApproveNotificationRequestBuilder()


class CancelApproveNotificationRequestBuilder(object):

    def __init__(self, cancel_approve_notification_request: CancelApproveNotificationRequest = CancelApproveNotificationRequest()) -> None:
        cancel_approve_notification_request.http_method = HttpMethod.POST
        cancel_approve_notification_request.uri = "/open-apis/helpdesk/v1/notifications/:notification_id/cancel_approve"
        cancel_approve_notification_request.token_types = {AccessTokenType.USER}
        self._cancel_approve_notification_request: CancelApproveNotificationRequest = cancel_approve_notification_request
    
    def notification_id(self, notification_id: str) -> "CancelApproveNotificationRequestBuilder":
        self._cancel_approve_notification_request.notification_id = notification_id
        self._cancel_approve_notification_request.paths["notification_id"] = notification_id
        return self
    

    def build(self) -> CancelApproveNotificationRequest:
        return self._cancel_approve_notification_request
