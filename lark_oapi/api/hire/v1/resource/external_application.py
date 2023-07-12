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
from lark_oapi.api.hire.v1.model.create_external_application_request import CreateExternalApplicationRequest
from lark_oapi.api.hire.v1.model.create_external_application_response import CreateExternalApplicationResponse
from lark_oapi.api.hire.v1.model.delete_external_application_request import DeleteExternalApplicationRequest
from lark_oapi.api.hire.v1.model.delete_external_application_response import DeleteExternalApplicationResponse
from lark_oapi.api.hire.v1.model.update_external_application_request import UpdateExternalApplicationRequest
from lark_oapi.api.hire.v1.model.update_external_application_response import UpdateExternalApplicationResponse


class ExternalApplication(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateExternalApplicationRequest, option: RequestOption = RequestOption()) -> CreateExternalApplicationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateExternalApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateExternalApplicationResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteExternalApplicationRequest, option: RequestOption = RequestOption()) -> DeleteExternalApplicationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteExternalApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteExternalApplicationResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateExternalApplicationRequest, option: RequestOption = RequestOption()) -> UpdateExternalApplicationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateExternalApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateExternalApplicationResponse)
        response.raw = resp

        return response

    
