# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .agent_schedule import AgentSchedule


class GetAgentSchedulesResponseBody(object):
    _types = {
        "agent_schedule": AgentSchedule,
    }

    def __init__(self, d):
        self.agent_schedule: Optional[AgentSchedule] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAgentSchedulesResponseBodyBuilder":
        return GetAgentSchedulesResponseBodyBuilder()


class GetAgentSchedulesResponseBodyBuilder(object):
    def __init__(self, get_agent_schedules_response_body: GetAgentSchedulesResponseBody = GetAgentSchedulesResponseBody({})) -> None:
        self._get_agent_schedules_response_body: GetAgentSchedulesResponseBody = get_agent_schedules_response_body
    
    def agent_schedule(self, agent_schedule: AgentSchedule) -> "GetAgentSchedulesResponseBodyBuilder":
        self._get_agent_schedules_response_body.agent_schedule = agent_schedule
        return self
    
    def build(self) -> "GetAgentSchedulesResponseBody":
        return self._get_agent_schedules_response_body