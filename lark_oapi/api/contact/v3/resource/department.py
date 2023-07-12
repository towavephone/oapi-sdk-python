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
from lark_oapi.api.contact.v3.model.batch_department_request import BatchDepartmentRequest
from lark_oapi.api.contact.v3.model.batch_department_response import BatchDepartmentResponse
from lark_oapi.api.contact.v3.model.children_department_request import ChildrenDepartmentRequest
from lark_oapi.api.contact.v3.model.children_department_response import ChildrenDepartmentResponse
from lark_oapi.api.contact.v3.model.create_department_request import CreateDepartmentRequest
from lark_oapi.api.contact.v3.model.create_department_response import CreateDepartmentResponse
from lark_oapi.api.contact.v3.model.delete_department_request import DeleteDepartmentRequest
from lark_oapi.api.contact.v3.model.delete_department_response import DeleteDepartmentResponse
from lark_oapi.api.contact.v3.model.get_department_request import GetDepartmentRequest
from lark_oapi.api.contact.v3.model.get_department_response import GetDepartmentResponse
from lark_oapi.api.contact.v3.model.list_department_request import ListDepartmentRequest
from lark_oapi.api.contact.v3.model.list_department_response import ListDepartmentResponse
from lark_oapi.api.contact.v3.model.parent_department_request import ParentDepartmentRequest
from lark_oapi.api.contact.v3.model.parent_department_response import ParentDepartmentResponse
from lark_oapi.api.contact.v3.model.patch_department_request import PatchDepartmentRequest
from lark_oapi.api.contact.v3.model.patch_department_response import PatchDepartmentResponse
from lark_oapi.api.contact.v3.model.search_department_request import SearchDepartmentRequest
from lark_oapi.api.contact.v3.model.search_department_response import SearchDepartmentResponse
from lark_oapi.api.contact.v3.model.unbind_department_chat_department_request import UnbindDepartmentChatDepartmentRequest
from lark_oapi.api.contact.v3.model.unbind_department_chat_department_response import UnbindDepartmentChatDepartmentResponse
from lark_oapi.api.contact.v3.model.update_department_request import UpdateDepartmentRequest
from lark_oapi.api.contact.v3.model.update_department_response import UpdateDepartmentResponse


class Department(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def batch(self, request: BatchDepartmentRequest, option: RequestOption = RequestOption()) -> BatchDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: BatchDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchDepartmentResponse)
        response.raw = resp

        return response

    def children(self, request: ChildrenDepartmentRequest, option: RequestOption = RequestOption()) -> ChildrenDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ChildrenDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), ChildrenDepartmentResponse)
        response.raw = resp

        return response

    def create(self, request: CreateDepartmentRequest, option: RequestOption = RequestOption()) -> CreateDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateDepartmentResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteDepartmentRequest, option: RequestOption = RequestOption()) -> DeleteDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteDepartmentResponse)
        response.raw = resp

        return response

    def get(self, request: GetDepartmentRequest, option: RequestOption = RequestOption()) -> GetDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), GetDepartmentResponse)
        response.raw = resp

        return response

    def list(self, request: ListDepartmentRequest, option: RequestOption = RequestOption()) -> ListDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), ListDepartmentResponse)
        response.raw = resp

        return response

    def parent(self, request: ParentDepartmentRequest, option: RequestOption = RequestOption()) -> ParentDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ParentDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), ParentDepartmentResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchDepartmentRequest, option: RequestOption = RequestOption()) -> PatchDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchDepartmentResponse)
        response.raw = resp

        return response

    def search(self, request: SearchDepartmentRequest, option: RequestOption = RequestOption()) -> SearchDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: SearchDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchDepartmentResponse)
        response.raw = resp

        return response

    def unbind_department_chat(self, request: UnbindDepartmentChatDepartmentRequest, option: RequestOption = RequestOption()) -> UnbindDepartmentChatDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UnbindDepartmentChatDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), UnbindDepartmentChatDepartmentResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateDepartmentRequest, option: RequestOption = RequestOption()) -> UpdateDepartmentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateDepartmentResponse)
        response.raw = resp

        return response

    
