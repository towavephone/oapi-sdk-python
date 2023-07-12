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
from lark_oapi.api.attendance.v1.model.batch_create_user_daily_shift_request import BatchCreateUserDailyShiftRequest
from lark_oapi.api.attendance.v1.model.batch_create_user_daily_shift_response import BatchCreateUserDailyShiftResponse
from lark_oapi.api.attendance.v1.model.query_user_daily_shift_request import QueryUserDailyShiftRequest
from lark_oapi.api.attendance.v1.model.query_user_daily_shift_response import QueryUserDailyShiftResponse


class UserDailyShift(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def batch_create(self, request: BatchCreateUserDailyShiftRequest, option: RequestOption = RequestOption()) -> BatchCreateUserDailyShiftResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: BatchCreateUserDailyShiftResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchCreateUserDailyShiftResponse)
        response.raw = resp

        return response

    def query(self, request: QueryUserDailyShiftRequest, option: RequestOption = RequestOption()) -> QueryUserDailyShiftResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: QueryUserDailyShiftResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryUserDailyShiftResponse)
        response.raw = resp

        return response

    
