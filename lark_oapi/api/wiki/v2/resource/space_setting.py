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
from lark_oapi.api.wiki.v2.model.update_space_setting_request import UpdateSpaceSettingRequest
from lark_oapi.api.wiki.v2.model.update_space_setting_response import UpdateSpaceSettingResponse


class SpaceSetting(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def update(self, request: UpdateSpaceSettingRequest, option: RequestOption = RequestOption()) -> UpdateSpaceSettingResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateSpaceSettingResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateSpaceSettingResponse)
        response.raw = resp

        return response

    
