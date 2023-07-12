# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .room_digital_signage import RoomDigitalSignage
from .room_digital_signage import RoomDigitalSignage
from .room_status import RoomStatus


class RoomConfig(object):
    _types = {
        "room_background": str,
        "display_background": str,
        "digital_signage": RoomDigitalSignage,
        "room_box_digital_signage": RoomDigitalSignage,
        "room_status": RoomStatus,
    }

    def __init__(self, d):
        self.room_background: Optional[str] = None
        self.display_background: Optional[str] = None
        self.digital_signage: Optional[RoomDigitalSignage] = None
        self.room_box_digital_signage: Optional[RoomDigitalSignage] = None
        self.room_status: Optional[RoomStatus] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RoomConfigBuilder":
        return RoomConfigBuilder()


class RoomConfigBuilder(object):
    def __init__(self, room_config: RoomConfig = RoomConfig({})) -> None:
        self._room_config: RoomConfig = room_config
    
    def room_background(self, room_background: str) -> "RoomConfigBuilder":
        self._room_config.room_background = room_background
        return self
    
    def display_background(self, display_background: str) -> "RoomConfigBuilder":
        self._room_config.display_background = display_background
        return self
    
    def digital_signage(self, digital_signage: RoomDigitalSignage) -> "RoomConfigBuilder":
        self._room_config.digital_signage = digital_signage
        return self
    
    def room_box_digital_signage(self, room_box_digital_signage: RoomDigitalSignage) -> "RoomConfigBuilder":
        self._room_config.room_box_digital_signage = room_box_digital_signage
        return self
    
    def room_status(self, room_status: RoomStatus) -> "RoomConfigBuilder":
        self._room_config.room_status = room_status
        return self
    
    def build(self) -> "RoomConfig":
        return self._room_config