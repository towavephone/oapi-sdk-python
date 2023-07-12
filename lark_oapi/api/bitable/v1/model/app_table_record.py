# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .person import Person
from .person import Person


class AppTableRecord(object):
    _types = {
        "record_id": str,
        "created_by": Person,
        "created_time": int,
        "last_modified_by": Person,
        "last_modified_time": int,
        "fields": Dict[str, Any],
    }

    def __init__(self, d):
        self.record_id: Optional[str] = None
        self.created_by: Optional[Person] = None
        self.created_time: Optional[int] = None
        self.last_modified_by: Optional[Person] = None
        self.last_modified_time: Optional[int] = None
        self.fields: Optional[Dict[str, Any]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableRecordBuilder":
        return AppTableRecordBuilder()


class AppTableRecordBuilder(object):
    def __init__(self, app_table_record: AppTableRecord = AppTableRecord({})) -> None:
        self._app_table_record: AppTableRecord = app_table_record
    
    def record_id(self, record_id: str) -> "AppTableRecordBuilder":
        self._app_table_record.record_id = record_id
        return self
    
    def created_by(self, created_by: Person) -> "AppTableRecordBuilder":
        self._app_table_record.created_by = created_by
        return self
    
    def created_time(self, created_time: int) -> "AppTableRecordBuilder":
        self._app_table_record.created_time = created_time
        return self
    
    def last_modified_by(self, last_modified_by: Person) -> "AppTableRecordBuilder":
        self._app_table_record.last_modified_by = last_modified_by
        return self
    
    def last_modified_time(self, last_modified_time: int) -> "AppTableRecordBuilder":
        self._app_table_record.last_modified_time = last_modified_time
        return self
    
    def fields(self, fields: Dict[str, Any]) -> "AppTableRecordBuilder":
        self._app_table_record.fields = fields
        return self
    
    def build(self) -> "AppTableRecord":
        return self._app_table_record