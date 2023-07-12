# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class InstanceCc(object):
    _types = {
        "approval_code": str,
        "instance_code": str,
        "user_id": str,
        "cc_user_ids": List[str],
        "comment": str,
    }

    def __init__(self, d):
        self.approval_code: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.user_id: Optional[str] = None
        self.cc_user_ids: Optional[List[str]] = None
        self.comment: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceCcBuilder":
        return InstanceCcBuilder()


class InstanceCcBuilder(object):
    def __init__(self, instance_cc: InstanceCc = InstanceCc({})) -> None:
        self._instance_cc: InstanceCc = instance_cc
    
    def approval_code(self, approval_code: str) -> "InstanceCcBuilder":
        self._instance_cc.approval_code = approval_code
        return self
    
    def instance_code(self, instance_code: str) -> "InstanceCcBuilder":
        self._instance_cc.instance_code = instance_code
        return self
    
    def user_id(self, user_id: str) -> "InstanceCcBuilder":
        self._instance_cc.user_id = user_id
        return self
    
    def cc_user_ids(self, cc_user_ids: List[str]) -> "InstanceCcBuilder":
        self._instance_cc.cc_user_ids = cc_user_ids
        return self
    
    def comment(self, comment: str) -> "InstanceCcBuilder":
        self._instance_cc.comment = comment
        return self
    
    def build(self) -> "InstanceCc":
        return self._instance_cc