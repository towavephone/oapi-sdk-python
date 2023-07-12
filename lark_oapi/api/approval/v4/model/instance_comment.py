# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .file import File


class InstanceComment(object):
    _types = {
        "id": str,
        "user_id": str,
        "open_id": str,
        "comment": str,
        "create_time": int,
        "files": List[File],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.open_id: Optional[str] = None
        self.comment: Optional[str] = None
        self.create_time: Optional[int] = None
        self.files: Optional[List[File]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceCommentBuilder":
        return InstanceCommentBuilder()


class InstanceCommentBuilder(object):
    def __init__(self, instance_comment: InstanceComment = InstanceComment({})) -> None:
        self._instance_comment: InstanceComment = instance_comment
    
    def id(self, id: str) -> "InstanceCommentBuilder":
        self._instance_comment.id = id
        return self
    
    def user_id(self, user_id: str) -> "InstanceCommentBuilder":
        self._instance_comment.user_id = user_id
        return self
    
    def open_id(self, open_id: str) -> "InstanceCommentBuilder":
        self._instance_comment.open_id = open_id
        return self
    
    def comment(self, comment: str) -> "InstanceCommentBuilder":
        self._instance_comment.comment = comment
        return self
    
    def create_time(self, create_time: int) -> "InstanceCommentBuilder":
        self._instance_comment.create_time = create_time
        return self
    
    def files(self, files: List[File]) -> "InstanceCommentBuilder":
        self._instance_comment.files = files
        return self
    
    def build(self) -> "InstanceComment":
        return self._instance_comment