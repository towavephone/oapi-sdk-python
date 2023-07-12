# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListByNoMeetingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.meeting_no: Optional[str] = None
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListByNoMeetingRequestBuilder":
        return ListByNoMeetingRequestBuilder()


class ListByNoMeetingRequestBuilder(object):

    def __init__(self, list_by_no_meeting_request: ListByNoMeetingRequest = ListByNoMeetingRequest()) -> None:
        list_by_no_meeting_request.http_method = HttpMethod.GET
        list_by_no_meeting_request.uri = "/open-apis/vc/v1/meetings/list_by_no"
        list_by_no_meeting_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_by_no_meeting_request: ListByNoMeetingRequest = list_by_no_meeting_request
    
    def meeting_no(self, meeting_no: str) -> "ListByNoMeetingRequestBuilder":
        self._list_by_no_meeting_request.meeting_no = meeting_no
        self._list_by_no_meeting_request.queries["meeting_no"] = str(meeting_no)
        return self
    
    def start_time(self, start_time: int) -> "ListByNoMeetingRequestBuilder":
        self._list_by_no_meeting_request.start_time = start_time
        self._list_by_no_meeting_request.queries["start_time"] = str(start_time)
        return self
    
    def end_time(self, end_time: int) -> "ListByNoMeetingRequestBuilder":
        self._list_by_no_meeting_request.end_time = end_time
        self._list_by_no_meeting_request.queries["end_time"] = str(end_time)
        return self
    
    def page_token(self, page_token: str) -> "ListByNoMeetingRequestBuilder":
        self._list_by_no_meeting_request.page_token = page_token
        self._list_by_no_meeting_request.queries["page_token"] = str(page_token)
        return self
    
    def page_size(self, page_size: int) -> "ListByNoMeetingRequestBuilder":
        self._list_by_no_meeting_request.page_size = page_size
        self._list_by_no_meeting_request.queries["page_size"] = str(page_size)
        return self
    

    def build(self) -> ListByNoMeetingRequest:
        return self._list_by_no_meeting_request
