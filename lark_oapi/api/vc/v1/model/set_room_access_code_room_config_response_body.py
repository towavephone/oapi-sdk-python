# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class SetRoomAccessCodeRoomConfigResponseBody(object):
    _types = {
        "access_code": str,
    }

    def __init__(self, d):
        self.access_code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SetRoomAccessCodeRoomConfigResponseBodyBuilder":
        return SetRoomAccessCodeRoomConfigResponseBodyBuilder()


class SetRoomAccessCodeRoomConfigResponseBodyBuilder(object):
    def __init__(self, set_room_access_code_room_config_response_body: SetRoomAccessCodeRoomConfigResponseBody = SetRoomAccessCodeRoomConfigResponseBody({})) -> None:
        self._set_room_access_code_room_config_response_body: SetRoomAccessCodeRoomConfigResponseBody = set_room_access_code_room_config_response_body
    
    def access_code(self, access_code: str) -> "SetRoomAccessCodeRoomConfigResponseBodyBuilder":
        self._set_room_access_code_room_config_response_body.access_code = access_code
        return self
    
    def build(self) -> "SetRoomAccessCodeRoomConfigResponseBody":
        return self._set_room_access_code_room_config_response_body