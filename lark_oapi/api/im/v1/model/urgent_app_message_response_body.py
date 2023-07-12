# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class UrgentAppMessageResponseBody(object):
    _types = {
        "invalid_user_id_list": List[str],
    }

    def __init__(self, d):
        self.invalid_user_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UrgentAppMessageResponseBodyBuilder":
        return UrgentAppMessageResponseBodyBuilder()


class UrgentAppMessageResponseBodyBuilder(object):
    def __init__(self, urgent_app_message_response_body: UrgentAppMessageResponseBody = UrgentAppMessageResponseBody({})) -> None:
        self._urgent_app_message_response_body: UrgentAppMessageResponseBody = urgent_app_message_response_body
    
    def invalid_user_id_list(self, invalid_user_id_list: List[str]) -> "UrgentAppMessageResponseBodyBuilder":
        self._urgent_app_message_response_body.invalid_user_id_list = invalid_user_id_list
        return self
    
    def build(self) -> "UrgentAppMessageResponseBody":
        return self._urgent_app_message_response_body