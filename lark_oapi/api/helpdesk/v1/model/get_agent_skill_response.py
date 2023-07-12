# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_agent_skill_response_body import GetAgentSkillResponseBody


class GetAgentSkillResponse(BaseResponse):
    _types = {
        "data": GetAgentSkillResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetAgentSkillResponseBody] = None
        init(self, d, self._types)
