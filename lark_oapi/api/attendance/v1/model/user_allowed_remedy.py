# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class UserAllowedRemedy(object):
    _types = {
        "user_id": str,
        "remedy_date": int,
        "is_free_punch": bool,
        "punch_no": int,
        "work_type": int,
        "punch_status": str,
        "normal_punch_time": str,
        "remedy_start_time": str,
        "remedy_end_time": str,
    }

    def __init__(self, d):
        self.user_id: Optional[str] = None
        self.remedy_date: Optional[int] = None
        self.is_free_punch: Optional[bool] = None
        self.punch_no: Optional[int] = None
        self.work_type: Optional[int] = None
        self.punch_status: Optional[str] = None
        self.normal_punch_time: Optional[str] = None
        self.remedy_start_time: Optional[str] = None
        self.remedy_end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserAllowedRemedyBuilder":
        return UserAllowedRemedyBuilder()


class UserAllowedRemedyBuilder(object):
    def __init__(self, user_allowed_remedy: UserAllowedRemedy = UserAllowedRemedy({})) -> None:
        self._user_allowed_remedy: UserAllowedRemedy = user_allowed_remedy
    
    def user_id(self, user_id: str) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.user_id = user_id
        return self
    
    def remedy_date(self, remedy_date: int) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.remedy_date = remedy_date
        return self
    
    def is_free_punch(self, is_free_punch: bool) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.is_free_punch = is_free_punch
        return self
    
    def punch_no(self, punch_no: int) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.punch_no = punch_no
        return self
    
    def work_type(self, work_type: int) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.work_type = work_type
        return self
    
    def punch_status(self, punch_status: str) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.punch_status = punch_status
        return self
    
    def normal_punch_time(self, normal_punch_time: str) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.normal_punch_time = normal_punch_time
        return self
    
    def remedy_start_time(self, remedy_start_time: str) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.remedy_start_time = remedy_start_time
        return self
    
    def remedy_end_time(self, remedy_end_time: str) -> "UserAllowedRemedyBuilder":
        self._user_allowed_remedy.remedy_end_time = remedy_end_time
        return self
    
    def build(self) -> "UserAllowedRemedy":
        return self._user_allowed_remedy