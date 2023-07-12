# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .app_table_form_field import AppTableFormField


class ListAppTableFormFieldResponseBody(object):
    _types = {
        "items": List[AppTableFormField],
        "page_token": str,
        "has_more": bool,
        "total": int,
    }

    def __init__(self, d):
        self.items: Optional[List[AppTableFormField]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        self.total: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAppTableFormFieldResponseBodyBuilder":
        return ListAppTableFormFieldResponseBodyBuilder()


class ListAppTableFormFieldResponseBodyBuilder(object):
    def __init__(self, list_app_table_form_field_response_body: ListAppTableFormFieldResponseBody = ListAppTableFormFieldResponseBody({})) -> None:
        self._list_app_table_form_field_response_body: ListAppTableFormFieldResponseBody = list_app_table_form_field_response_body
    
    def items(self, items: List[AppTableFormField]) -> "ListAppTableFormFieldResponseBodyBuilder":
        self._list_app_table_form_field_response_body.items = items
        return self
    
    def page_token(self, page_token: str) -> "ListAppTableFormFieldResponseBodyBuilder":
        self._list_app_table_form_field_response_body.page_token = page_token
        return self
    
    def has_more(self, has_more: bool) -> "ListAppTableFormFieldResponseBodyBuilder":
        self._list_app_table_form_field_response_body.has_more = has_more
        return self
    
    def total(self, total: int) -> "ListAppTableFormFieldResponseBodyBuilder":
        self._list_app_table_form_field_response_body.total = total
        return self
    
    def build(self) -> "ListAppTableFormFieldResponseBody":
        return self._list_app_table_form_field_response_body