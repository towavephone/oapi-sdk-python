# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .user_id import UserId


class RoomStatusEvent(object):
    _types = {
        "status": bool,
        "schedule_status": bool,
        "disable_start_time": int,
        "disable_end_time": int,
        "disable_reason": str,
        "contact_ids": List[UserId],
        "disable_notice": bool,
        "resume_notice": bool,
    }

    def __init__(self, d):
        self.status: Optional[bool] = None
        self.schedule_status: Optional[bool] = None
        self.disable_start_time: Optional[int] = None
        self.disable_end_time: Optional[int] = None
        self.disable_reason: Optional[str] = None
        self.contact_ids: Optional[List[UserId]] = None
        self.disable_notice: Optional[bool] = None
        self.resume_notice: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RoomStatusEventBuilder":
        return RoomStatusEventBuilder()


class RoomStatusEventBuilder(object):
    def __init__(self, room_status_event: RoomStatusEvent = RoomStatusEvent({})) -> None:
        self._room_status_event: RoomStatusEvent = room_status_event
    
    def status(self, status: bool) -> "RoomStatusEventBuilder":
        self._room_status_event.status = status
        return self
    
    def schedule_status(self, schedule_status: bool) -> "RoomStatusEventBuilder":
        self._room_status_event.schedule_status = schedule_status
        return self
    
    def disable_start_time(self, disable_start_time: int) -> "RoomStatusEventBuilder":
        self._room_status_event.disable_start_time = disable_start_time
        return self
    
    def disable_end_time(self, disable_end_time: int) -> "RoomStatusEventBuilder":
        self._room_status_event.disable_end_time = disable_end_time
        return self
    
    def disable_reason(self, disable_reason: str) -> "RoomStatusEventBuilder":
        self._room_status_event.disable_reason = disable_reason
        return self
    
    def contact_ids(self, contact_ids: List[UserId]) -> "RoomStatusEventBuilder":
        self._room_status_event.contact_ids = contact_ids
        return self
    
    def disable_notice(self, disable_notice: bool) -> "RoomStatusEventBuilder":
        self._room_status_event.disable_notice = disable_notice
        return self
    
    def resume_notice(self, resume_notice: bool) -> "RoomStatusEventBuilder":
        self._room_status_event.resume_notice = resume_notice
        return self
    
    def build(self) -> "RoomStatusEvent":
        return self._room_status_event