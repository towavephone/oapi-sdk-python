# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .user_flow import UserFlow


class BatchCreateUserFlowResponseBody(object):
    _types = {
        "flow_records": List[UserFlow],
    }

    def __init__(self, d):
        self.flow_records: Optional[List[UserFlow]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateUserFlowResponseBodyBuilder":
        return BatchCreateUserFlowResponseBodyBuilder()


class BatchCreateUserFlowResponseBodyBuilder(object):
    def __init__(self, batch_create_user_flow_response_body: BatchCreateUserFlowResponseBody = BatchCreateUserFlowResponseBody({})) -> None:
        self._batch_create_user_flow_response_body: BatchCreateUserFlowResponseBody = batch_create_user_flow_response_body
    
    def flow_records(self, flow_records: List[UserFlow]) -> "BatchCreateUserFlowResponseBodyBuilder":
        self._batch_create_user_flow_response_body.flow_records = flow_records
        return self
    
    def build(self) -> "BatchCreateUserFlowResponseBody":
        return self._batch_create_user_flow_response_body