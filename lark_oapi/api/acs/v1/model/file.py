# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class File(object):
    _types = {
        "files": IO[Any],
        "file_type": str,
        "file_name": str,
    }

    def __init__(self, d):
        self.files: Optional[IO[Any]] = None
        self.file_type: Optional[str] = None
        self.file_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileBuilder":
        return FileBuilder()


class FileBuilder(object):
    def __init__(self, file: File = File({})) -> None:
        self._file: File = file
    
    def files(self, files: IO[Any]) -> "FileBuilder":
        self._file.files = files
        return self
    
    def file_type(self, file_type: str) -> "FileBuilder":
        self._file.file_type = file_type
        return self
    
    def file_name(self, file_name: str) -> "FileBuilder":
        self._file.file_name = file_name
        return self
    
    def build(self) -> "File":
        return self._file