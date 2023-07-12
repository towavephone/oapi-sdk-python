# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CheckWhiteBlackListApplicationVisibilityRequestBody(object):
    _types = {
        "user_ids": List[str],
        "department_ids": List[str],
        "group_ids": List[str],
    }

    def __init__(self, d):
        self.user_ids: Optional[List[str]] = None
        self.department_ids: Optional[List[str]] = None
        self.group_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder":
        return CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder()


class CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder(object):
    def __init__(self, check_white_black_list_application_visibility_request_body: CheckWhiteBlackListApplicationVisibilityRequestBody = CheckWhiteBlackListApplicationVisibilityRequestBody({})) -> None:
        self._check_white_black_list_application_visibility_request_body: CheckWhiteBlackListApplicationVisibilityRequestBody = check_white_black_list_application_visibility_request_body
    
    def user_ids(self, user_ids: List[str]) -> "CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder":
        self._check_white_black_list_application_visibility_request_body.user_ids = user_ids
        return self
    
    def department_ids(self, department_ids: List[str]) -> "CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder":
        self._check_white_black_list_application_visibility_request_body.department_ids = department_ids
        return self
    
    def group_ids(self, group_ids: List[str]) -> "CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder":
        self._check_white_black_list_application_visibility_request_body.group_ids = group_ids
        return self
    
    def build(self) -> "CheckWhiteBlackListApplicationVisibilityRequestBody":
        return self._check_white_black_list_application_visibility_request_body