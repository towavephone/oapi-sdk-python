# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .device import Device


class ListDeviceResponseBody(object):
    _types = {
        "items": List[Device],
    }

    def __init__(self, d):
        self.items: Optional[List[Device]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListDeviceResponseBodyBuilder":
        return ListDeviceResponseBodyBuilder()


class ListDeviceResponseBodyBuilder(object):
    def __init__(self, list_device_response_body: ListDeviceResponseBody = ListDeviceResponseBody({})) -> None:
        self._list_device_response_body: ListDeviceResponseBody = list_device_response_body
    
    def items(self, items: List[Device]) -> "ListDeviceResponseBodyBuilder":
        self._list_device_response_body.items = items
        return self
    
    def build(self) -> "ListDeviceResponseBody":
        return self._list_device_response_body