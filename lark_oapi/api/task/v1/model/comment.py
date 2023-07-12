# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Comment(object):
    _types = {
        "content": str,
        "parent_id": int,
        "id": int,
        "create_milli_time": int,
        "rich_content": str,
        "creator_id": str,
    }

    def __init__(self, d):
        self.content: Optional[str] = None
        self.parent_id: Optional[int] = None
        self.id: Optional[int] = None
        self.create_milli_time: Optional[int] = None
        self.rich_content: Optional[str] = None
        self.creator_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommentBuilder":
        return CommentBuilder()


class CommentBuilder(object):
    def __init__(self, comment: Comment = Comment({})) -> None:
        self._comment: Comment = comment
    
    def content(self, content: str) -> "CommentBuilder":
        self._comment.content = content
        return self
    
    def parent_id(self, parent_id: int) -> "CommentBuilder":
        self._comment.parent_id = parent_id
        return self
    
    def id(self, id: int) -> "CommentBuilder":
        self._comment.id = id
        return self
    
    def create_milli_time(self, create_milli_time: int) -> "CommentBuilder":
        self._comment.create_milli_time = create_milli_time
        return self
    
    def rich_content(self, rich_content: str) -> "CommentBuilder":
        self._comment.rich_content = rich_content
        return self
    
    def creator_id(self, creator_id: str) -> "CommentBuilder":
        self._comment.creator_id = creator_id
        return self
    
    def build(self) -> "Comment":
        return self._comment