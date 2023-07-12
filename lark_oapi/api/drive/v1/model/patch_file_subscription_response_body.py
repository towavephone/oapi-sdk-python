# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .file_subscription import FileSubscription


class PatchFileSubscriptionResponseBody(object):
    _types = {
        "subscription": FileSubscription,
    }

    def __init__(self, d):
        self.subscription: Optional[FileSubscription] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchFileSubscriptionResponseBodyBuilder":
        return PatchFileSubscriptionResponseBodyBuilder()


class PatchFileSubscriptionResponseBodyBuilder(object):
    def __init__(self, patch_file_subscription_response_body: PatchFileSubscriptionResponseBody = PatchFileSubscriptionResponseBody({})) -> None:
        self._patch_file_subscription_response_body: PatchFileSubscriptionResponseBody = patch_file_subscription_response_body
    
    def subscription(self, subscription: FileSubscription) -> "PatchFileSubscriptionResponseBodyBuilder":
        self._patch_file_subscription_response_body.subscription = subscription
        return self
    
    def build(self) -> "PatchFileSubscriptionResponseBody":
        return self._patch_file_subscription_response_body