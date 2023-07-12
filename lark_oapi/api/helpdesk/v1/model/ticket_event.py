# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .ticket_user_event import TicketUserEvent
from .ticket_user_event import TicketUserEvent
from .ticket_user_event import TicketUserEvent
from .ticket_user_event import TicketUserEvent
from .customized_field_display_item import CustomizedFieldDisplayItem


class TicketEvent(object):
    _types = {
        "ticket_id": str,
        "helpdesk_id": str,
        "guest": TicketUserEvent,
        "stage": int,
        "status": int,
        "score": int,
        "created_at": int,
        "updated_at": int,
        "closed_at": int,
        "agents": List[TicketUserEvent],
        "channel": int,
        "solve": int,
        "closed_by": TicketUserEvent,
        "collaborators": List[TicketUserEvent],
        "customized_fields": List[CustomizedFieldDisplayItem],
        "chat_id": str,
    }

    def __init__(self, d):
        self.ticket_id: Optional[str] = None
        self.helpdesk_id: Optional[str] = None
        self.guest: Optional[TicketUserEvent] = None
        self.stage: Optional[int] = None
        self.status: Optional[int] = None
        self.score: Optional[int] = None
        self.created_at: Optional[int] = None
        self.updated_at: Optional[int] = None
        self.closed_at: Optional[int] = None
        self.agents: Optional[List[TicketUserEvent]] = None
        self.channel: Optional[int] = None
        self.solve: Optional[int] = None
        self.closed_by: Optional[TicketUserEvent] = None
        self.collaborators: Optional[List[TicketUserEvent]] = None
        self.customized_fields: Optional[List[CustomizedFieldDisplayItem]] = None
        self.chat_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TicketEventBuilder":
        return TicketEventBuilder()


class TicketEventBuilder(object):
    def __init__(self, ticket_event: TicketEvent = TicketEvent({})) -> None:
        self._ticket_event: TicketEvent = ticket_event
    
    def ticket_id(self, ticket_id: str) -> "TicketEventBuilder":
        self._ticket_event.ticket_id = ticket_id
        return self
    
    def helpdesk_id(self, helpdesk_id: str) -> "TicketEventBuilder":
        self._ticket_event.helpdesk_id = helpdesk_id
        return self
    
    def guest(self, guest: TicketUserEvent) -> "TicketEventBuilder":
        self._ticket_event.guest = guest
        return self
    
    def stage(self, stage: int) -> "TicketEventBuilder":
        self._ticket_event.stage = stage
        return self
    
    def status(self, status: int) -> "TicketEventBuilder":
        self._ticket_event.status = status
        return self
    
    def score(self, score: int) -> "TicketEventBuilder":
        self._ticket_event.score = score
        return self
    
    def created_at(self, created_at: int) -> "TicketEventBuilder":
        self._ticket_event.created_at = created_at
        return self
    
    def updated_at(self, updated_at: int) -> "TicketEventBuilder":
        self._ticket_event.updated_at = updated_at
        return self
    
    def closed_at(self, closed_at: int) -> "TicketEventBuilder":
        self._ticket_event.closed_at = closed_at
        return self
    
    def agents(self, agents: List[TicketUserEvent]) -> "TicketEventBuilder":
        self._ticket_event.agents = agents
        return self
    
    def channel(self, channel: int) -> "TicketEventBuilder":
        self._ticket_event.channel = channel
        return self
    
    def solve(self, solve: int) -> "TicketEventBuilder":
        self._ticket_event.solve = solve
        return self
    
    def closed_by(self, closed_by: TicketUserEvent) -> "TicketEventBuilder":
        self._ticket_event.closed_by = closed_by
        return self
    
    def collaborators(self, collaborators: List[TicketUserEvent]) -> "TicketEventBuilder":
        self._ticket_event.collaborators = collaborators
        return self
    
    def customized_fields(self, customized_fields: List[CustomizedFieldDisplayItem]) -> "TicketEventBuilder":
        self._ticket_event.customized_fields = customized_fields
        return self
    
    def chat_id(self, chat_id: str) -> "TicketEventBuilder":
        self._ticket_event.chat_id = chat_id
        return self
    
    def build(self) -> "TicketEvent":
        return self._ticket_event