# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListTicketRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.ticket_id: Optional[str] = None
        self.agent_id: Optional[str] = None
        self.closed_by_id: Optional[str] = None
        self.type: Optional[int] = None
        self.channel: Optional[int] = None
        self.solved: Optional[int] = None
        self.score: Optional[int] = None
        self.status_list: Optional[List[int]] = None
        self.guest_name: Optional[str] = None
        self.guest_id: Optional[str] = None
        self.tags: Optional[List[str]] = None
        self.page: Optional[int] = None
        self.page_size: Optional[int] = None
        self.create_time_start: Optional[int] = None
        self.create_time_end: Optional[int] = None
        self.update_time_start: Optional[int] = None
        self.update_time_end: Optional[int] = None

    @staticmethod
    def builder() -> "ListTicketRequestBuilder":
        return ListTicketRequestBuilder()


class ListTicketRequestBuilder(object):

    def __init__(self, list_ticket_request: ListTicketRequest = ListTicketRequest()) -> None:
        list_ticket_request.http_method = HttpMethod.GET
        list_ticket_request.uri = "/open-apis/helpdesk/v1/tickets"
        list_ticket_request.token_types = {AccessTokenType.TENANT}
        self._list_ticket_request: ListTicketRequest = list_ticket_request
    
    def ticket_id(self, ticket_id: str) -> "ListTicketRequestBuilder":
        self._list_ticket_request.ticket_id = ticket_id
        self._list_ticket_request.queries["ticket_id"] = str(ticket_id)
        return self
    
    def agent_id(self, agent_id: str) -> "ListTicketRequestBuilder":
        self._list_ticket_request.agent_id = agent_id
        self._list_ticket_request.queries["agent_id"] = str(agent_id)
        return self
    
    def closed_by_id(self, closed_by_id: str) -> "ListTicketRequestBuilder":
        self._list_ticket_request.closed_by_id = closed_by_id
        self._list_ticket_request.queries["closed_by_id"] = str(closed_by_id)
        return self
    
    def type(self, type: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.type = type
        self._list_ticket_request.queries["type"] = str(type)
        return self
    
    def channel(self, channel: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.channel = channel
        self._list_ticket_request.queries["channel"] = str(channel)
        return self
    
    def solved(self, solved: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.solved = solved
        self._list_ticket_request.queries["solved"] = str(solved)
        return self
    
    def score(self, score: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.score = score
        self._list_ticket_request.queries["score"] = str(score)
        return self
    
    def status_list(self, status_list: List[int]) -> "ListTicketRequestBuilder":
        self._list_ticket_request.status_list = status_list
        self._list_ticket_request.queries["status_list"] = str(status_list)
        return self
    
    def guest_name(self, guest_name: str) -> "ListTicketRequestBuilder":
        self._list_ticket_request.guest_name = guest_name
        self._list_ticket_request.queries["guest_name"] = str(guest_name)
        return self
    
    def guest_id(self, guest_id: str) -> "ListTicketRequestBuilder":
        self._list_ticket_request.guest_id = guest_id
        self._list_ticket_request.queries["guest_id"] = str(guest_id)
        return self
    
    def tags(self, tags: List[str]) -> "ListTicketRequestBuilder":
        self._list_ticket_request.tags = tags
        self._list_ticket_request.queries["tags"] = str(tags)
        return self
    
    def page(self, page: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.page = page
        self._list_ticket_request.queries["page"] = str(page)
        return self
    
    def page_size(self, page_size: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.page_size = page_size
        self._list_ticket_request.queries["page_size"] = str(page_size)
        return self
    
    def create_time_start(self, create_time_start: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.create_time_start = create_time_start
        self._list_ticket_request.queries["create_time_start"] = str(create_time_start)
        return self
    
    def create_time_end(self, create_time_end: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.create_time_end = create_time_end
        self._list_ticket_request.queries["create_time_end"] = str(create_time_end)
        return self
    
    def update_time_start(self, update_time_start: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.update_time_start = update_time_start
        self._list_ticket_request.queries["update_time_start"] = str(update_time_start)
        return self
    
    def update_time_end(self, update_time_end: int) -> "ListTicketRequestBuilder":
        self._list_ticket_request.update_time_end = update_time_end
        self._list_ticket_request.queries["update_time_end"] = str(update_time_end)
        return self
    

    def build(self) -> ListTicketRequest:
        return self._list_ticket_request
