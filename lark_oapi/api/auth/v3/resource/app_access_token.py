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
from lark_oapi.api.auth.v3.model.create_app_access_token_request import CreateAppAccessTokenRequest
from lark_oapi.api.auth.v3.model.create_app_access_token_response import CreateAppAccessTokenResponse
from lark_oapi.api.auth.v3.model.internal_app_access_token_request import InternalAppAccessTokenRequest
from lark_oapi.api.auth.v3.model.internal_app_access_token_response import InternalAppAccessTokenResponse


class AppAccessToken(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateAppAccessTokenRequest, option: RequestOption = RequestOption()) -> CreateAppAccessTokenResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateAppAccessTokenResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAppAccessTokenResponse)
        response.raw = resp

        return response

    def internal(self, request: InternalAppAccessTokenRequest, option: RequestOption = RequestOption()) -> InternalAppAccessTokenResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: InternalAppAccessTokenResponse = JSON.unmarshal(str(resp.content, UTF_8), InternalAppAccessTokenResponse)
        response.raw = resp

        return response

    
