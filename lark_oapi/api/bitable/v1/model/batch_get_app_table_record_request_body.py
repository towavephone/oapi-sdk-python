# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BatchGetAppTableRecordRequestBody(object):
    _types = {
        "record_ids": List[str],
        "user_id_type": str,
        "with_shared_url": bool,
        "automatic_fields": bool,
    }

    def __init__(self, d=None):
        self.record_ids: Optional[List[str]] = None
        self.user_id_type: Optional[str] = None
        self.with_shared_url: Optional[bool] = None
        self.automatic_fields: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchGetAppTableRecordRequestBodyBuilder":
        return BatchGetAppTableRecordRequestBodyBuilder()


class BatchGetAppTableRecordRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_get_app_table_record_request_body = BatchGetAppTableRecordRequestBody()

    def record_ids(self, record_ids: List[str]) -> "BatchGetAppTableRecordRequestBodyBuilder":
        self._batch_get_app_table_record_request_body.record_ids = record_ids
        return self

    def user_id_type(self, user_id_type: str) -> "BatchGetAppTableRecordRequestBodyBuilder":
        self._batch_get_app_table_record_request_body.user_id_type = user_id_type
        return self

    def with_shared_url(self, with_shared_url: bool) -> "BatchGetAppTableRecordRequestBodyBuilder":
        self._batch_get_app_table_record_request_body.with_shared_url = with_shared_url
        return self

    def automatic_fields(self, automatic_fields: bool) -> "BatchGetAppTableRecordRequestBodyBuilder":
        self._batch_get_app_table_record_request_body.automatic_fields = automatic_fields
        return self

    def build(self) -> "BatchGetAppTableRecordRequestBody":
        return self._batch_get_app_table_record_request_body
