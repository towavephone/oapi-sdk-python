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
from lark_oapi.api.hire.v1.model.list_job_requirement_schema_request import ListJobRequirementSchemaRequest
from lark_oapi.api.hire.v1.model.list_job_requirement_schema_response import ListJobRequirementSchemaResponse


class JobRequirementSchema(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def list(self, request: ListJobRequirementSchemaRequest, option: RequestOption = RequestOption()) -> ListJobRequirementSchemaResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListJobRequirementSchemaResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobRequirementSchemaResponse)
        response.raw = resp

        return response

    
