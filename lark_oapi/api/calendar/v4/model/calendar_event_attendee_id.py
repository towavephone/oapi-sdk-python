# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CalendarEventAttendeeId(object):
    _types = {
        "type": str,
        "attendee_id": str,
        "user_id": str,
        "chat_id": str,
        "room_id": str,
        "third_party_email": str,
    }

    def __init__(self, d):
        self.type: Optional[str] = None
        self.attendee_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.room_id: Optional[str] = None
        self.third_party_email: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CalendarEventAttendeeIdBuilder":
        return CalendarEventAttendeeIdBuilder()


class CalendarEventAttendeeIdBuilder(object):
    def __init__(self, calendar_event_attendee_id: CalendarEventAttendeeId = CalendarEventAttendeeId({})) -> None:
        self._calendar_event_attendee_id: CalendarEventAttendeeId = calendar_event_attendee_id
    
    def type(self, type: str) -> "CalendarEventAttendeeIdBuilder":
        self._calendar_event_attendee_id.type = type
        return self
    
    def attendee_id(self, attendee_id: str) -> "CalendarEventAttendeeIdBuilder":
        self._calendar_event_attendee_id.attendee_id = attendee_id
        return self
    
    def user_id(self, user_id: str) -> "CalendarEventAttendeeIdBuilder":
        self._calendar_event_attendee_id.user_id = user_id
        return self
    
    def chat_id(self, chat_id: str) -> "CalendarEventAttendeeIdBuilder":
        self._calendar_event_attendee_id.chat_id = chat_id
        return self
    
    def room_id(self, room_id: str) -> "CalendarEventAttendeeIdBuilder":
        self._calendar_event_attendee_id.room_id = room_id
        return self
    
    def third_party_email(self, third_party_email: str) -> "CalendarEventAttendeeIdBuilder":
        self._calendar_event_attendee_id.third_party_email = third_party_email
        return self
    
    def build(self) -> "CalendarEventAttendeeId":
        return self._calendar_event_attendee_id