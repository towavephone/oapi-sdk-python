# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class JobDetailTag(object):
    _types = {
        "id": str,
        "name": I18n,
        "order": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.order: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDetailTagBuilder":
        return JobDetailTagBuilder()


class JobDetailTagBuilder(object):
    def __init__(self) -> None:
        self._job_detail_tag = JobDetailTag()

    def id(self, id: str) -> "JobDetailTagBuilder":
        self._job_detail_tag.id = id
        return self

    def name(self, name: I18n) -> "JobDetailTagBuilder":
        self._job_detail_tag.name = name
        return self

    def order(self, order: int) -> "JobDetailTagBuilder":
        self._job_detail_tag.order = order
        return self

    def build(self) -> "JobDetailTag":
        return self._job_detail_tag
