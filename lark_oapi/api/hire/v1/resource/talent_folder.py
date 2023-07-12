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
from lark_oapi.api.hire.v1.model.list_talent_folder_request import ListTalentFolderRequest
from lark_oapi.api.hire.v1.model.list_talent_folder_response import ListTalentFolderResponse


class TalentFolder(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def list(self, request: ListTalentFolderRequest, option: RequestOption = RequestOption()) -> ListTalentFolderResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListTalentFolderResponse = JSON.unmarshal(str(resp.content, UTF_8), ListTalentFolderResponse)
        response.raw = resp

        return response

    
