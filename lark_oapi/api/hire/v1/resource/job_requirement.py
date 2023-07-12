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
from lark_oapi.api.hire.v1.model.create_job_requirement_request import CreateJobRequirementRequest
from lark_oapi.api.hire.v1.model.create_job_requirement_response import CreateJobRequirementResponse
from lark_oapi.api.hire.v1.model.delete_job_requirement_request import DeleteJobRequirementRequest
from lark_oapi.api.hire.v1.model.delete_job_requirement_response import DeleteJobRequirementResponse
from lark_oapi.api.hire.v1.model.list_job_requirement_request import ListJobRequirementRequest
from lark_oapi.api.hire.v1.model.list_job_requirement_response import ListJobRequirementResponse
from lark_oapi.api.hire.v1.model.list_by_id_job_requirement_request import ListByIdJobRequirementRequest
from lark_oapi.api.hire.v1.model.list_by_id_job_requirement_response import ListByIdJobRequirementResponse
from lark_oapi.api.hire.v1.model.update_job_requirement_request import UpdateJobRequirementRequest
from lark_oapi.api.hire.v1.model.update_job_requirement_response import UpdateJobRequirementResponse


class JobRequirement(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateJobRequirementRequest, option: RequestOption = RequestOption()) -> CreateJobRequirementResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateJobRequirementResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteJobRequirementRequest, option: RequestOption = RequestOption()) -> DeleteJobRequirementResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteJobRequirementResponse)
        response.raw = resp

        return response

    def list(self, request: ListJobRequirementRequest, option: RequestOption = RequestOption()) -> ListJobRequirementResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobRequirementResponse)
        response.raw = resp

        return response

    def list_by_id(self, request: ListByIdJobRequirementRequest, option: RequestOption = RequestOption()) -> ListByIdJobRequirementResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListByIdJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), ListByIdJobRequirementResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateJobRequirementRequest, option: RequestOption = RequestOption()) -> UpdateJobRequirementResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateJobRequirementResponse)
        response.raw = resp

        return response

    
