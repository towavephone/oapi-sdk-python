# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListInterviewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.application_id: Optional[str] = None
        self.interview_id: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListInterviewRequestBuilder":
        return ListInterviewRequestBuilder()


class ListInterviewRequestBuilder(object):

    def __init__(self, list_interview_request: ListInterviewRequest = ListInterviewRequest()) -> None:
        list_interview_request.http_method = HttpMethod.GET
        list_interview_request.uri = "/open-apis/hire/v1/interviews"
        list_interview_request.token_types = {AccessTokenType.TENANT}
        self._list_interview_request: ListInterviewRequest = list_interview_request
    
    def page_size(self, page_size: int) -> "ListInterviewRequestBuilder":
        self._list_interview_request.page_size = page_size
        self._list_interview_request.queries["page_size"] = str(page_size)
        return self
    
    def page_token(self, page_token: str) -> "ListInterviewRequestBuilder":
        self._list_interview_request.page_token = page_token
        self._list_interview_request.queries["page_token"] = str(page_token)
        return self
    
    def application_id(self, application_id: str) -> "ListInterviewRequestBuilder":
        self._list_interview_request.application_id = application_id
        self._list_interview_request.queries["application_id"] = str(application_id)
        return self
    
    def interview_id(self, interview_id: str) -> "ListInterviewRequestBuilder":
        self._list_interview_request.interview_id = interview_id
        self._list_interview_request.queries["interview_id"] = str(interview_id)
        return self
    
    def start_time(self, start_time: str) -> "ListInterviewRequestBuilder":
        self._list_interview_request.start_time = start_time
        self._list_interview_request.queries["start_time"] = str(start_time)
        return self
    
    def end_time(self, end_time: str) -> "ListInterviewRequestBuilder":
        self._list_interview_request.end_time = end_time
        self._list_interview_request.queries["end_time"] = str(end_time)
        return self
    
    def user_id_type(self, user_id_type: str) -> "ListInterviewRequestBuilder":
        self._list_interview_request.user_id_type = user_id_type
        self._list_interview_request.queries["user_id_type"] = str(user_id_type)
        return self
    

    def build(self) -> ListInterviewRequest:
        return self._list_interview_request
