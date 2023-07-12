# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .task import Task


class CreateTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[Task] = None

    @staticmethod
    def builder() -> "CreateTaskRequestBuilder":
        return CreateTaskRequestBuilder()


class CreateTaskRequestBuilder(object):

    def __init__(self, create_task_request: CreateTaskRequest = CreateTaskRequest()) -> None:
        create_task_request.http_method = HttpMethod.POST
        create_task_request.uri = "/open-apis/task/v1/tasks"
        create_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_task_request: CreateTaskRequest = create_task_request
    
    def user_id_type(self, user_id_type: str) -> "CreateTaskRequestBuilder":
        self._create_task_request.user_id_type = user_id_type
        self._create_task_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def request_body(self, request_body: Task) -> "CreateTaskRequestBuilder":
        self._create_task_request.request_body = request_body
        self._create_task_request.body = request_body
        return self

    def build(self) -> CreateTaskRequest:
        return self._create_task_request
