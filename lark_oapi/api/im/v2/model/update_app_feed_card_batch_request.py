# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .update_app_feed_card_batch_request_body import UpdateAppFeedCardBatchRequestBody


class UpdateAppFeedCardBatchRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[UpdateAppFeedCardBatchRequestBody] = None

    @staticmethod
    def builder() -> "UpdateAppFeedCardBatchRequestBuilder":
        return UpdateAppFeedCardBatchRequestBuilder()


class UpdateAppFeedCardBatchRequestBuilder(object):

    def __init__(self) -> None:
        update_app_feed_card_batch_request = UpdateAppFeedCardBatchRequest()
        update_app_feed_card_batch_request.http_method = HttpMethod.PUT
        update_app_feed_card_batch_request.uri = "/open-apis/im/v2/app_feed_card/batch"
        update_app_feed_card_batch_request.token_types = {AccessTokenType.TENANT}
        self._update_app_feed_card_batch_request: UpdateAppFeedCardBatchRequest = update_app_feed_card_batch_request

    def user_id_type(self, user_id_type: str) -> "UpdateAppFeedCardBatchRequestBuilder":
        self._update_app_feed_card_batch_request.user_id_type = user_id_type
        self._update_app_feed_card_batch_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: UpdateAppFeedCardBatchRequestBody) -> "UpdateAppFeedCardBatchRequestBuilder":
        self._update_app_feed_card_batch_request.request_body = request_body
        self._update_app_feed_card_batch_request.body = request_body
        return self

    def build(self) -> UpdateAppFeedCardBatchRequest:
        return self._update_app_feed_card_batch_request
