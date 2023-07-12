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
from lark_oapi.api.contact.v3.model.create_employee_type_enum_request import CreateEmployeeTypeEnumRequest
from lark_oapi.api.contact.v3.model.create_employee_type_enum_response import CreateEmployeeTypeEnumResponse
from lark_oapi.api.contact.v3.model.delete_employee_type_enum_request import DeleteEmployeeTypeEnumRequest
from lark_oapi.api.contact.v3.model.delete_employee_type_enum_response import DeleteEmployeeTypeEnumResponse
from lark_oapi.api.contact.v3.model.list_employee_type_enum_request import ListEmployeeTypeEnumRequest
from lark_oapi.api.contact.v3.model.list_employee_type_enum_response import ListEmployeeTypeEnumResponse
from lark_oapi.api.contact.v3.model.update_employee_type_enum_request import UpdateEmployeeTypeEnumRequest
from lark_oapi.api.contact.v3.model.update_employee_type_enum_response import UpdateEmployeeTypeEnumResponse


class EmployeeTypeEnum(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateEmployeeTypeEnumRequest, option: RequestOption = RequestOption()) -> CreateEmployeeTypeEnumResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateEmployeeTypeEnumResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateEmployeeTypeEnumResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteEmployeeTypeEnumRequest, option: RequestOption = RequestOption()) -> DeleteEmployeeTypeEnumResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteEmployeeTypeEnumResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteEmployeeTypeEnumResponse)
        response.raw = resp

        return response

    def list(self, request: ListEmployeeTypeEnumRequest, option: RequestOption = RequestOption()) -> ListEmployeeTypeEnumResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListEmployeeTypeEnumResponse = JSON.unmarshal(str(resp.content, UTF_8), ListEmployeeTypeEnumResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateEmployeeTypeEnumRequest, option: RequestOption = RequestOption()) -> UpdateEmployeeTypeEnumResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateEmployeeTypeEnumResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateEmployeeTypeEnumResponse)
        response.raw = resp

        return response

    
