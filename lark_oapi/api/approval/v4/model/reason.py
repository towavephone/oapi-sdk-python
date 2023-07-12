# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .file import File


class Reason(object):
    _types = {
        "text": str,
        "files": List[File],
    }

    def __init__(self, d):
        self.text: Optional[str] = None
        self.files: Optional[List[File]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReasonBuilder":
        return ReasonBuilder()


class ReasonBuilder(object):
    def __init__(self, reason: Reason = Reason({})) -> None:
        self._reason: Reason = reason
    
    def text(self, text: str) -> "ReasonBuilder":
        self._reason.text = text
        return self
    
    def files(self, files: List[File]) -> "ReasonBuilder":
        self._reason.files = files
        return self
    
    def build(self) -> "Reason":
        return self._reason