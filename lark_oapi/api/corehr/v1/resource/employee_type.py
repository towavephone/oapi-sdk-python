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
from lark_oapi.api.corehr.v1.model.create_employee_type_request import CreateEmployeeTypeRequest
from lark_oapi.api.corehr.v1.model.create_employee_type_response import CreateEmployeeTypeResponse
from lark_oapi.api.corehr.v1.model.delete_employee_type_request import DeleteEmployeeTypeRequest
from lark_oapi.api.corehr.v1.model.delete_employee_type_response import DeleteEmployeeTypeResponse
from lark_oapi.api.corehr.v1.model.get_employee_type_request import GetEmployeeTypeRequest
from lark_oapi.api.corehr.v1.model.get_employee_type_response import GetEmployeeTypeResponse
from lark_oapi.api.corehr.v1.model.list_employee_type_request import ListEmployeeTypeRequest
from lark_oapi.api.corehr.v1.model.list_employee_type_response import ListEmployeeTypeResponse
from lark_oapi.api.corehr.v1.model.patch_employee_type_request import PatchEmployeeTypeRequest
from lark_oapi.api.corehr.v1.model.patch_employee_type_response import PatchEmployeeTypeResponse


class EmployeeType(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateEmployeeTypeRequest, option: RequestOption = RequestOption()) -> CreateEmployeeTypeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateEmployeeTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateEmployeeTypeResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteEmployeeTypeRequest, option: RequestOption = RequestOption()) -> DeleteEmployeeTypeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteEmployeeTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteEmployeeTypeResponse)
        response.raw = resp

        return response

    def get(self, request: GetEmployeeTypeRequest, option: RequestOption = RequestOption()) -> GetEmployeeTypeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetEmployeeTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), GetEmployeeTypeResponse)
        response.raw = resp

        return response

    def list(self, request: ListEmployeeTypeRequest, option: RequestOption = RequestOption()) -> ListEmployeeTypeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListEmployeeTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), ListEmployeeTypeResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchEmployeeTypeRequest, option: RequestOption = RequestOption()) -> PatchEmployeeTypeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchEmployeeTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchEmployeeTypeResponse)
        response.raw = resp

        return response

    
