# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_agent_skill_rule_response_body import ListAgentSkillRuleResponseBody


class ListAgentSkillRuleResponse(BaseResponse):
    _types = {
        "data": ListAgentSkillRuleResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListAgentSkillRuleResponseBody] = None
        init(self, d, self._types)
