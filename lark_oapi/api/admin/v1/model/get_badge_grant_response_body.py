# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .grant import Grant


class GetBadgeGrantResponseBody(object):
    _types = {
        "grant": Grant,
    }

    def __init__(self, d):
        self.grant: Optional[Grant] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetBadgeGrantResponseBodyBuilder":
        return GetBadgeGrantResponseBodyBuilder()


class GetBadgeGrantResponseBodyBuilder(object):
    def __init__(self, get_badge_grant_response_body: GetBadgeGrantResponseBody = GetBadgeGrantResponseBody({})) -> None:
        self._get_badge_grant_response_body: GetBadgeGrantResponseBody = get_badge_grant_response_body
    
    def grant(self, grant: Grant) -> "GetBadgeGrantResponseBodyBuilder":
        self._get_badge_grant_response_body.grant = grant
        return self
    
    def build(self) -> "GetBadgeGrantResponseBody":
        return self._get_badge_grant_response_body