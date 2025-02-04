# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class WkCalendarDate(object):
    _types = {
        "calendar_id": str,
        "date": str,
        "date_type": str,
        "id": str,
    }

    def __init__(self, d=None):
        self.calendar_id: Optional[str] = None
        self.date: Optional[str] = None
        self.date_type: Optional[str] = None
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WkCalendarDateBuilder":
        return WkCalendarDateBuilder()


class WkCalendarDateBuilder(object):
    def __init__(self) -> None:
        self._wk_calendar_date = WkCalendarDate()

    def calendar_id(self, calendar_id: str) -> "WkCalendarDateBuilder":
        self._wk_calendar_date.calendar_id = calendar_id
        return self

    def date(self, date: str) -> "WkCalendarDateBuilder":
        self._wk_calendar_date.date = date
        return self

    def date_type(self, date_type: str) -> "WkCalendarDateBuilder":
        self._wk_calendar_date.date_type = date_type
        return self

    def id(self, id: str) -> "WkCalendarDateBuilder":
        self._wk_calendar_date.id = id
        return self

    def build(self) -> "WkCalendarDate":
        return self._wk_calendar_date
