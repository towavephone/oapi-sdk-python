# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class TaskAssignee(object):
    _types = {
        "id": str,
        "completed_at": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.completed_at: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskAssigneeBuilder":
        return TaskAssigneeBuilder()


class TaskAssigneeBuilder(object):
    def __init__(self) -> None:
        self._task_assignee = TaskAssignee()

    def id(self, id: str) -> "TaskAssigneeBuilder":
        self._task_assignee.id = id
        return self

    def completed_at(self, completed_at: int) -> "TaskAssigneeBuilder":
        self._task_assignee.completed_at = completed_at
        return self

    def build(self) -> "TaskAssignee":
        return self._task_assignee
