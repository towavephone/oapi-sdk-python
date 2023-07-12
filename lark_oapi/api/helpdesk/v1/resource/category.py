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
from lark_oapi.api.helpdesk.v1.model.create_category_request import CreateCategoryRequest
from lark_oapi.api.helpdesk.v1.model.create_category_response import CreateCategoryResponse
from lark_oapi.api.helpdesk.v1.model.delete_category_request import DeleteCategoryRequest
from lark_oapi.api.helpdesk.v1.model.delete_category_response import DeleteCategoryResponse
from lark_oapi.api.helpdesk.v1.model.get_category_request import GetCategoryRequest
from lark_oapi.api.helpdesk.v1.model.get_category_response import GetCategoryResponse
from lark_oapi.api.helpdesk.v1.model.list_category_request import ListCategoryRequest
from lark_oapi.api.helpdesk.v1.model.list_category_response import ListCategoryResponse
from lark_oapi.api.helpdesk.v1.model.patch_category_request import PatchCategoryRequest
from lark_oapi.api.helpdesk.v1.model.patch_category_response import PatchCategoryResponse


class Category(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateCategoryRequest, option: RequestOption = RequestOption()) -> CreateCategoryResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateCategoryResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateCategoryResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteCategoryRequest, option: RequestOption = RequestOption()) -> DeleteCategoryResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteCategoryResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteCategoryResponse)
        response.raw = resp

        return response

    def get(self, request: GetCategoryRequest, option: RequestOption = RequestOption()) -> GetCategoryResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetCategoryResponse = JSON.unmarshal(str(resp.content, UTF_8), GetCategoryResponse)
        response.raw = resp

        return response

    def list(self, request: ListCategoryRequest, option: RequestOption = RequestOption()) -> ListCategoryResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListCategoryResponse = JSON.unmarshal(str(resp.content, UTF_8), ListCategoryResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchCategoryRequest, option: RequestOption = RequestOption()) -> PatchCategoryResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchCategoryResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchCategoryResponse)
        response.raw = resp

        return response

    
