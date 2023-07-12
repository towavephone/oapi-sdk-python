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
from lark_oapi.api.corehr.v1.model.create_employment_request import CreateEmploymentRequest
from lark_oapi.api.corehr.v1.model.create_employment_response import CreateEmploymentResponse
from lark_oapi.api.corehr.v1.model.delete_employment_request import DeleteEmploymentRequest
from lark_oapi.api.corehr.v1.model.delete_employment_response import DeleteEmploymentResponse
from lark_oapi.api.corehr.v1.model.patch_employment_request import PatchEmploymentRequest
from lark_oapi.api.corehr.v1.model.patch_employment_response import PatchEmploymentResponse


class Employment(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateEmploymentRequest, option: RequestOption = RequestOption()) -> CreateEmploymentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateEmploymentResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateEmploymentResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteEmploymentRequest, option: RequestOption = RequestOption()) -> DeleteEmploymentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteEmploymentResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteEmploymentResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchEmploymentRequest, option: RequestOption = RequestOption()) -> PatchEmploymentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchEmploymentResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchEmploymentResponse)
        response.raw = resp

        return response

    
