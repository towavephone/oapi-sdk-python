# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_workforce_plan_detail_request_body import BatchWorkforcePlanDetailRequestBody


class BatchWorkforcePlanDetailRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.request_body: Optional[BatchWorkforcePlanDetailRequestBody] = None

    @staticmethod
    def builder() -> "BatchWorkforcePlanDetailRequestBuilder":
        return BatchWorkforcePlanDetailRequestBuilder()


class BatchWorkforcePlanDetailRequestBuilder(object):

    def __init__(self) -> None:
        batch_workforce_plan_detail_request = BatchWorkforcePlanDetailRequest()
        batch_workforce_plan_detail_request.http_method = HttpMethod.POST
        batch_workforce_plan_detail_request.uri = "/open-apis/corehr/v2/workforce_plan_details/batch"
        batch_workforce_plan_detail_request.token_types = {AccessTokenType.TENANT}
        self._batch_workforce_plan_detail_request: BatchWorkforcePlanDetailRequest = batch_workforce_plan_detail_request

    def page_token(self, page_token: str) -> "BatchWorkforcePlanDetailRequestBuilder":
        self._batch_workforce_plan_detail_request.page_token = page_token
        self._batch_workforce_plan_detail_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "BatchWorkforcePlanDetailRequestBuilder":
        self._batch_workforce_plan_detail_request.page_size = page_size
        self._batch_workforce_plan_detail_request.add_query("page_size", page_size)
        return self

    def request_body(self,
                     request_body: BatchWorkforcePlanDetailRequestBody) -> "BatchWorkforcePlanDetailRequestBuilder":
        self._batch_workforce_plan_detail_request.request_body = request_body
        self._batch_workforce_plan_detail_request.body = request_body
        return self

    def build(self) -> BatchWorkforcePlanDetailRequest:
        return self._batch_workforce_plan_detail_request
