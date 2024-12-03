# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_external_referral_reward_response_body import CreateExternalReferralRewardResponseBody


class CreateExternalReferralRewardResponse(BaseResponse):
    _types = {
        "data": CreateExternalReferralRewardResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateExternalReferralRewardResponseBody] = None
        init(self, d, self._types)
