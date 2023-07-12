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
from lark_oapi.api.corehr.v1.model.create_job_request import CreateJobRequest
from lark_oapi.api.corehr.v1.model.create_job_response import CreateJobResponse
from lark_oapi.api.corehr.v1.model.delete_job_request import DeleteJobRequest
from lark_oapi.api.corehr.v1.model.delete_job_response import DeleteJobResponse
from lark_oapi.api.corehr.v1.model.get_job_request import GetJobRequest
from lark_oapi.api.corehr.v1.model.get_job_response import GetJobResponse
from lark_oapi.api.corehr.v1.model.list_job_request import ListJobRequest
from lark_oapi.api.corehr.v1.model.list_job_response import ListJobResponse
from lark_oapi.api.corehr.v1.model.patch_job_request import PatchJobRequest
from lark_oapi.api.corehr.v1.model.patch_job_response import PatchJobResponse


class Job(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateJobRequest, option: RequestOption = RequestOption()) -> CreateJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateJobResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateJobResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteJobRequest, option: RequestOption = RequestOption()) -> DeleteJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteJobResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteJobResponse)
        response.raw = resp

        return response

    def get(self, request: GetJobRequest, option: RequestOption = RequestOption()) -> GetJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetJobResponse = JSON.unmarshal(str(resp.content, UTF_8), GetJobResponse)
        response.raw = resp

        return response

    def list(self, request: ListJobRequest, option: RequestOption = RequestOption()) -> ListJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListJobResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchJobRequest, option: RequestOption = RequestOption()) -> PatchJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchJobResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchJobResponse)
        response.raw = resp

        return response

    
