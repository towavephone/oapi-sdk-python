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
from lark_oapi.api.calendar.v4.model.batch_delete_calendar_event_attendee_request import BatchDeleteCalendarEventAttendeeRequest
from lark_oapi.api.calendar.v4.model.batch_delete_calendar_event_attendee_response import BatchDeleteCalendarEventAttendeeResponse
from lark_oapi.api.calendar.v4.model.create_calendar_event_attendee_request import CreateCalendarEventAttendeeRequest
from lark_oapi.api.calendar.v4.model.create_calendar_event_attendee_response import CreateCalendarEventAttendeeResponse
from lark_oapi.api.calendar.v4.model.list_calendar_event_attendee_request import ListCalendarEventAttendeeRequest
from lark_oapi.api.calendar.v4.model.list_calendar_event_attendee_response import ListCalendarEventAttendeeResponse


class CalendarEventAttendee(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def batch_delete(self, request: BatchDeleteCalendarEventAttendeeRequest, option: RequestOption = RequestOption()) -> BatchDeleteCalendarEventAttendeeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: BatchDeleteCalendarEventAttendeeResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchDeleteCalendarEventAttendeeResponse)
        response.raw = resp

        return response

    def create(self, request: CreateCalendarEventAttendeeRequest, option: RequestOption = RequestOption()) -> CreateCalendarEventAttendeeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateCalendarEventAttendeeResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateCalendarEventAttendeeResponse)
        response.raw = resp

        return response

    def list(self, request: ListCalendarEventAttendeeRequest, option: RequestOption = RequestOption()) -> ListCalendarEventAttendeeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListCalendarEventAttendeeResponse = JSON.unmarshal(str(resp.content, UTF_8), ListCalendarEventAttendeeResponse)
        response.raw = resp

        return response

    
