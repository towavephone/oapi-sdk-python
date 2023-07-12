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
from lark_oapi.api.hire.v1.model.patch_ehr_import_task_request import PatchEhrImportTaskRequest
from lark_oapi.api.hire.v1.model.patch_ehr_import_task_response import PatchEhrImportTaskResponse


class EhrImportTask(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def patch(self, request: PatchEhrImportTaskRequest, option: RequestOption = RequestOption()) -> PatchEhrImportTaskResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchEhrImportTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchEhrImportTaskResponse)
        response.raw = resp

        return response

    
