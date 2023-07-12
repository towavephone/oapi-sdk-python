# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v1.resource import *


class HelpdeskService(object):
    def __init__(self, config: Config) -> None:
        self.v1: V1 = V1(config)


class V1(object):
    def __init__(self, config: Config) -> None:
        self.agent: Optional[Agent] = Agent(config)
        self.agent_schedules: Optional[AgentSchedules] = AgentSchedules(config)
        self.agent_schedule: Optional[AgentSchedule] = AgentSchedule(config)
        self.agent_skill: Optional[AgentSkill] = AgentSkill(config)
        self.agent_skill_rule: Optional[AgentSkillRule] = AgentSkillRule(config)
        self.bot_message: Optional[BotMessage] = BotMessage(config)
        self.category: Optional[Category] = Category(config)
        self.event: Optional[Event] = Event(config)
        self.faq: Optional[Faq] = Faq(config)
        self.notification: Optional[Notification] = Notification(config)
        self.ticket: Optional[Ticket] = Ticket(config)
        self.ticket_message: Optional[TicketMessage] = TicketMessage(config)
        self.ticket_customized_field: Optional[TicketCustomizedField] = TicketCustomizedField(config)