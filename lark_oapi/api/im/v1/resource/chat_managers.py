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
from lark_oapi.api.im.v1.model.add_managers_chat_managers_request import AddManagersChatManagersRequest
from lark_oapi.api.im.v1.model.add_managers_chat_managers_response import AddManagersChatManagersResponse
from lark_oapi.api.im.v1.model.delete_managers_chat_managers_request import DeleteManagersChatManagersRequest
from lark_oapi.api.im.v1.model.delete_managers_chat_managers_response import DeleteManagersChatManagersResponse


class ChatManagers(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def add_managers(self, request: AddManagersChatManagersRequest, option: RequestOption = RequestOption()) -> AddManagersChatManagersResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: AddManagersChatManagersResponse = JSON.unmarshal(str(resp.content, UTF_8), AddManagersChatManagersResponse)
        response.raw = resp

        return response

    def delete_managers(self, request: DeleteManagersChatManagersRequest, option: RequestOption = RequestOption()) -> DeleteManagersChatManagersResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteManagersChatManagersResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteManagersChatManagersResponse)
        response.raw = resp

        return response

    
