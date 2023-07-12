# Code generated by Lark OpenAPI.

import io
from typing import *
from typing import IO
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from lark_oapi.api.helpdesk.v1.model.delete_agent_schedules_request import DeleteAgentSchedulesRequest
from lark_oapi.api.helpdesk.v1.model.delete_agent_schedules_response import DeleteAgentSchedulesResponse
from lark_oapi.api.helpdesk.v1.model.get_agent_schedules_request import GetAgentSchedulesRequest
from lark_oapi.api.helpdesk.v1.model.get_agent_schedules_response import GetAgentSchedulesResponse
from lark_oapi.api.helpdesk.v1.model.patch_agent_schedules_request import PatchAgentSchedulesRequest
from lark_oapi.api.helpdesk.v1.model.patch_agent_schedules_response import PatchAgentSchedulesResponse


class AgentSchedules(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def delete(self, request: DeleteAgentSchedulesRequest, option: RequestOption = RequestOption()) -> DeleteAgentSchedulesResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteAgentSchedulesResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteAgentSchedulesResponse)
        response.raw = resp

        return response

    def get(self, request: GetAgentSchedulesRequest, option: RequestOption = RequestOption()) -> GetAgentSchedulesResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetAgentSchedulesResponse = JSON.unmarshal(str(resp.content, UTF_8), GetAgentSchedulesResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchAgentSchedulesRequest, option: RequestOption = RequestOption()) -> PatchAgentSchedulesResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchAgentSchedulesResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchAgentSchedulesResponse)
        response.raw = resp

        return response

    
