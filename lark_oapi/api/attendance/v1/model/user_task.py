# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .task_result import TaskResult


class UserTask(object):
    _types = {
        "result_id": str,
        "user_id": str,
        "employee_name": str,
        "day": int,
        "group_id": str,
        "shift_id": str,
        "records": List[TaskResult],
    }

    def __init__(self, d):
        self.result_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.employee_name: Optional[str] = None
        self.day: Optional[int] = None
        self.group_id: Optional[str] = None
        self.shift_id: Optional[str] = None
        self.records: Optional[List[TaskResult]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserTaskBuilder":
        return UserTaskBuilder()


class UserTaskBuilder(object):
    def __init__(self, user_task: UserTask = UserTask({})) -> None:
        self._user_task: UserTask = user_task
    
    def result_id(self, result_id: str) -> "UserTaskBuilder":
        self._user_task.result_id = result_id
        return self
    
    def user_id(self, user_id: str) -> "UserTaskBuilder":
        self._user_task.user_id = user_id
        return self
    
    def employee_name(self, employee_name: str) -> "UserTaskBuilder":
        self._user_task.employee_name = employee_name
        return self
    
    def day(self, day: int) -> "UserTaskBuilder":
        self._user_task.day = day
        return self
    
    def group_id(self, group_id: str) -> "UserTaskBuilder":
        self._user_task.group_id = group_id
        return self
    
    def shift_id(self, shift_id: str) -> "UserTaskBuilder":
        self._user_task.shift_id = shift_id
        return self
    
    def records(self, records: List[TaskResult]) -> "UserTaskBuilder":
        self._user_task.records = records
        return self
    
    def build(self) -> "UserTask":
        return self._user_task