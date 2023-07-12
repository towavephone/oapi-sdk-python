# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Device(object):
    _types = {
        "name": str,
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeviceBuilder":
        return DeviceBuilder()


class DeviceBuilder(object):
    def __init__(self, device: Device = Device({})) -> None:
        self._device: Device = device
    
    def name(self, name: str) -> "DeviceBuilder":
        self._device.name = name
        return self
    
    def build(self) -> "Device":
        return self._device