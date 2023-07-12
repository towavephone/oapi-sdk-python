# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ApprovalInfo(object):
    _types = {
        "approval_id": str,
        "approval_type": str,
        "status": int,
    }

    def __init__(self, d):
        self.approval_id: Optional[str] = None
        self.approval_type: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalInfoBuilder":
        return ApprovalInfoBuilder()


class ApprovalInfoBuilder(object):
    def __init__(self, approval_info: ApprovalInfo = ApprovalInfo({})) -> None:
        self._approval_info: ApprovalInfo = approval_info
    
    def approval_id(self, approval_id: str) -> "ApprovalInfoBuilder":
        self._approval_info.approval_id = approval_id
        return self
    
    def approval_type(self, approval_type: str) -> "ApprovalInfoBuilder":
        self._approval_info.approval_type = approval_type
        return self
    
    def status(self, status: int) -> "ApprovalInfoBuilder":
        self._approval_info.status = status
        return self
    
    def build(self) -> "ApprovalInfo":
        return self._approval_info