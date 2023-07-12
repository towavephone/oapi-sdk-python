# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetUserFlowRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.user_flow_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetUserFlowRequestBuilder":
        return GetUserFlowRequestBuilder()


class GetUserFlowRequestBuilder(object):

    def __init__(self, get_user_flow_request: GetUserFlowRequest = GetUserFlowRequest()) -> None:
        get_user_flow_request.http_method = HttpMethod.GET
        get_user_flow_request.uri = "/open-apis/attendance/v1/user_flows/:user_flow_id"
        get_user_flow_request.token_types = {AccessTokenType.TENANT}
        self._get_user_flow_request: GetUserFlowRequest = get_user_flow_request
    
    def employee_type(self, employee_type: str) -> "GetUserFlowRequestBuilder":
        self._get_user_flow_request.employee_type = employee_type
        self._get_user_flow_request.queries["employee_type"] = str(employee_type)
        return self
    
    def user_flow_id(self, user_flow_id: str) -> "GetUserFlowRequestBuilder":
        self._get_user_flow_request.user_flow_id = user_flow_id
        self._get_user_flow_request.paths["user_flow_id"] = user_flow_id
        return self
    

    def build(self) -> GetUserFlowRequest:
        return self._get_user_flow_request
