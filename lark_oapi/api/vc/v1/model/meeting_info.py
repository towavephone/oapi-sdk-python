# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class MeetingInfo(object):
    _types = {
        "meeting_id": str,
        "meeting_topic": str,
        "organizer": str,
        "department": str,
        "user_id": str,
        "employee_id": str,
        "email": str,
        "mobile": str,
        "meeting_start_time": str,
        "meeting_end_time": str,
        "meeting_duration": str,
        "number_of_participants": str,
        "audio": bool,
        "video": bool,
        "sharing": bool,
        "recording": bool,
        "telephone": bool,
    }

    def __init__(self, d):
        self.meeting_id: Optional[str] = None
        self.meeting_topic: Optional[str] = None
        self.organizer: Optional[str] = None
        self.department: Optional[str] = None
        self.user_id: Optional[str] = None
        self.employee_id: Optional[str] = None
        self.email: Optional[str] = None
        self.mobile: Optional[str] = None
        self.meeting_start_time: Optional[str] = None
        self.meeting_end_time: Optional[str] = None
        self.meeting_duration: Optional[str] = None
        self.number_of_participants: Optional[str] = None
        self.audio: Optional[bool] = None
        self.video: Optional[bool] = None
        self.sharing: Optional[bool] = None
        self.recording: Optional[bool] = None
        self.telephone: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MeetingInfoBuilder":
        return MeetingInfoBuilder()


class MeetingInfoBuilder(object):
    def __init__(self, meeting_info: MeetingInfo = MeetingInfo({})) -> None:
        self._meeting_info: MeetingInfo = meeting_info
    
    def meeting_id(self, meeting_id: str) -> "MeetingInfoBuilder":
        self._meeting_info.meeting_id = meeting_id
        return self
    
    def meeting_topic(self, meeting_topic: str) -> "MeetingInfoBuilder":
        self._meeting_info.meeting_topic = meeting_topic
        return self
    
    def organizer(self, organizer: str) -> "MeetingInfoBuilder":
        self._meeting_info.organizer = organizer
        return self
    
    def department(self, department: str) -> "MeetingInfoBuilder":
        self._meeting_info.department = department
        return self
    
    def user_id(self, user_id: str) -> "MeetingInfoBuilder":
        self._meeting_info.user_id = user_id
        return self
    
    def employee_id(self, employee_id: str) -> "MeetingInfoBuilder":
        self._meeting_info.employee_id = employee_id
        return self
    
    def email(self, email: str) -> "MeetingInfoBuilder":
        self._meeting_info.email = email
        return self
    
    def mobile(self, mobile: str) -> "MeetingInfoBuilder":
        self._meeting_info.mobile = mobile
        return self
    
    def meeting_start_time(self, meeting_start_time: str) -> "MeetingInfoBuilder":
        self._meeting_info.meeting_start_time = meeting_start_time
        return self
    
    def meeting_end_time(self, meeting_end_time: str) -> "MeetingInfoBuilder":
        self._meeting_info.meeting_end_time = meeting_end_time
        return self
    
    def meeting_duration(self, meeting_duration: str) -> "MeetingInfoBuilder":
        self._meeting_info.meeting_duration = meeting_duration
        return self
    
    def number_of_participants(self, number_of_participants: str) -> "MeetingInfoBuilder":
        self._meeting_info.number_of_participants = number_of_participants
        return self
    
    def audio(self, audio: bool) -> "MeetingInfoBuilder":
        self._meeting_info.audio = audio
        return self
    
    def video(self, video: bool) -> "MeetingInfoBuilder":
        self._meeting_info.video = video
        return self
    
    def sharing(self, sharing: bool) -> "MeetingInfoBuilder":
        self._meeting_info.sharing = sharing
        return self
    
    def recording(self, recording: bool) -> "MeetingInfoBuilder":
        self._meeting_info.recording = recording
        return self
    
    def telephone(self, telephone: bool) -> "MeetingInfoBuilder":
        self._meeting_info.telephone = telephone
        return self
    
    def build(self) -> "MeetingInfo":
        return self._meeting_info