# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class CreateCalendarEventMeetingMinuteRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.calendar_id: Optional[str] = None
        self.event_id: Optional[str] = None

    @staticmethod
    def builder() -> "CreateCalendarEventMeetingMinuteRequestBuilder":
        return CreateCalendarEventMeetingMinuteRequestBuilder()


class CreateCalendarEventMeetingMinuteRequestBuilder(object):

    def __init__(self) -> None:
        create_calendar_event_meeting_minute_request = CreateCalendarEventMeetingMinuteRequest()
        create_calendar_event_meeting_minute_request.http_method = HttpMethod.POST
        create_calendar_event_meeting_minute_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id/meeting_minute"
        create_calendar_event_meeting_minute_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_calendar_event_meeting_minute_request: CreateCalendarEventMeetingMinuteRequest = create_calendar_event_meeting_minute_request

    def calendar_id(self, calendar_id: str) -> "CreateCalendarEventMeetingMinuteRequestBuilder":
        self._create_calendar_event_meeting_minute_request.calendar_id = calendar_id
        self._create_calendar_event_meeting_minute_request.paths["calendar_id"] = str(calendar_id)
        return self

    def event_id(self, event_id: str) -> "CreateCalendarEventMeetingMinuteRequestBuilder":
        self._create_calendar_event_meeting_minute_request.event_id = event_id
        self._create_calendar_event_meeting_minute_request.paths["event_id"] = str(event_id)
        return self

    def build(self) -> CreateCalendarEventMeetingMinuteRequest:
        return self._create_calendar_event_meeting_minute_request
