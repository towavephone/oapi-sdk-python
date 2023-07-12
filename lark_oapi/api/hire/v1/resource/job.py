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
from lark_oapi.api.hire.v1.model.combined_create_job_request import CombinedCreateJobRequest
from lark_oapi.api.hire.v1.model.combined_create_job_response import CombinedCreateJobResponse
from lark_oapi.api.hire.v1.model.combined_update_job_request import CombinedUpdateJobRequest
from lark_oapi.api.hire.v1.model.combined_update_job_response import CombinedUpdateJobResponse
from lark_oapi.api.hire.v1.model.config_job_request import ConfigJobRequest
from lark_oapi.api.hire.v1.model.config_job_response import ConfigJobResponse
from lark_oapi.api.hire.v1.model.get_job_request import GetJobRequest
from lark_oapi.api.hire.v1.model.get_job_response import GetJobResponse
from lark_oapi.api.hire.v1.model.update_config_job_request import UpdateConfigJobRequest
from lark_oapi.api.hire.v1.model.update_config_job_response import UpdateConfigJobResponse


class Job(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def combined_create(self, request: CombinedCreateJobRequest, option: RequestOption = RequestOption()) -> CombinedCreateJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CombinedCreateJobResponse = JSON.unmarshal(str(resp.content, UTF_8), CombinedCreateJobResponse)
        response.raw = resp

        return response

    def combined_update(self, request: CombinedUpdateJobRequest, option: RequestOption = RequestOption()) -> CombinedUpdateJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CombinedUpdateJobResponse = JSON.unmarshal(str(resp.content, UTF_8), CombinedUpdateJobResponse)
        response.raw = resp

        return response

    def config(self, request: ConfigJobRequest, option: RequestOption = RequestOption()) -> ConfigJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ConfigJobResponse = JSON.unmarshal(str(resp.content, UTF_8), ConfigJobResponse)
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

    def update_config(self, request: UpdateConfigJobRequest, option: RequestOption = RequestOption()) -> UpdateConfigJobResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateConfigJobResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateConfigJobResponse)
        response.raw = resp

        return response

    
