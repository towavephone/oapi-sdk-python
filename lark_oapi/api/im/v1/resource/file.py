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
from lark_oapi.api.im.v1.model.create_file_request import CreateFileRequest
from lark_oapi.api.im.v1.model.create_file_response import CreateFileResponse
from lark_oapi.api.im.v1.model.get_file_request import GetFileRequest
from lark_oapi.api.im.v1.model.get_file_response import GetFileResponse


class File(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateFileRequest, option: RequestOption = RequestOption()) -> CreateFileResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 处理 form-data
        if request.body is not None:
            form_data = MultipartEncoder(Files.parse_form_data(request.body))
            option.headers[CONTENT_TYPE] = form_data.content_type
            request.body = form_data
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateFileResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateFileResponse)
        response.raw = resp

        return response

    def get(self, request: GetFileRequest, option: RequestOption = RequestOption()) -> GetFileResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 处理二进制流
        if resp.status_code == 200:
            response: GetFileResponse = GetFileResponse({})
            response.code = 0
            response.raw = resp
            response.file = io.BytesIO(resp.content)
            response.file_name = Files.parse_file_name(response.raw.header)
            return response
        
        # 反序列化
        response: GetFileResponse = JSON.unmarshal(str(resp.content, UTF_8), GetFileResponse)
        response.raw = resp

        return response

    
