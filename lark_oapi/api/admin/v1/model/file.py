# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .user import User


class File(object):
    _types = {
        "title": str,
        "type": str,
        "owner": User,
        "size": str,
        "last_op_time": str,
        "status": str,
        "token": str,
    }

    def __init__(self, d):
        self.title: Optional[str] = None
        self.type: Optional[str] = None
        self.owner: Optional[User] = None
        self.size: Optional[str] = None
        self.last_op_time: Optional[str] = None
        self.status: Optional[str] = None
        self.token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileBuilder":
        return FileBuilder()


class FileBuilder(object):
    def __init__(self, file: File = File({})) -> None:
        self._file: File = file
    
    def title(self, title: str) -> "FileBuilder":
        self._file.title = title
        return self
    
    def type(self, type: str) -> "FileBuilder":
        self._file.type = type
        return self
    
    def owner(self, owner: User) -> "FileBuilder":
        self._file.owner = owner
        return self
    
    def size(self, size: str) -> "FileBuilder":
        self._file.size = size
        return self
    
    def last_op_time(self, last_op_time: str) -> "FileBuilder":
        self._file.last_op_time = last_op_time
        return self
    
    def status(self, status: str) -> "FileBuilder":
        self._file.status = status
        return self
    
    def token(self, token: str) -> "FileBuilder":
        self._file.token = token
        return self
    
    def build(self) -> "File":
        return self._file