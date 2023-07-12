# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class DeleteAppTableFieldResponseBody(object):
    _types = {
        "field_id": str,
        "deleted": bool,
    }

    def __init__(self, d):
        self.field_id: Optional[str] = None
        self.deleted: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteAppTableFieldResponseBodyBuilder":
        return DeleteAppTableFieldResponseBodyBuilder()


class DeleteAppTableFieldResponseBodyBuilder(object):
    def __init__(self, delete_app_table_field_response_body: DeleteAppTableFieldResponseBody = DeleteAppTableFieldResponseBody({})) -> None:
        self._delete_app_table_field_response_body: DeleteAppTableFieldResponseBody = delete_app_table_field_response_body
    
    def field_id(self, field_id: str) -> "DeleteAppTableFieldResponseBodyBuilder":
        self._delete_app_table_field_response_body.field_id = field_id
        return self
    
    def deleted(self, deleted: bool) -> "DeleteAppTableFieldResponseBodyBuilder":
        self._delete_app_table_field_response_body.deleted = deleted
        return self
    
    def build(self) -> "DeleteAppTableFieldResponseBody":
        return self._delete_app_table_field_response_body