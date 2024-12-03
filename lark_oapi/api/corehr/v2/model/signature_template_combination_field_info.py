# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .signature_template_combination_sub_field_info import SignatureTemplateCombinationSubFieldInfo
from .enum import Enum


class SignatureTemplateCombinationFieldInfo(object):
    _types = {
        "total_apiname": str,
        "apiname": str,
        "title": List[I18n],
        "contents": List[list],
        "source": Enum,
    }

    def __init__(self, d=None):
        self.total_apiname: Optional[str] = None
        self.apiname: Optional[str] = None
        self.title: Optional[List[I18n]] = None
        self.contents: Optional[List[list]] = None
        self.source: Optional[Enum] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SignatureTemplateCombinationFieldInfoBuilder":
        return SignatureTemplateCombinationFieldInfoBuilder()


class SignatureTemplateCombinationFieldInfoBuilder(object):
    def __init__(self) -> None:
        self._signature_template_combination_field_info = SignatureTemplateCombinationFieldInfo()

    def total_apiname(self, total_apiname: str) -> "SignatureTemplateCombinationFieldInfoBuilder":
        self._signature_template_combination_field_info.total_apiname = total_apiname
        return self

    def apiname(self, apiname: str) -> "SignatureTemplateCombinationFieldInfoBuilder":
        self._signature_template_combination_field_info.apiname = apiname
        return self

    def title(self, title: List[I18n]) -> "SignatureTemplateCombinationFieldInfoBuilder":
        self._signature_template_combination_field_info.title = title
        return self

    def contents(self, contents: List[list]) -> "SignatureTemplateCombinationFieldInfoBuilder":
        self._signature_template_combination_field_info.contents = contents
        return self

    def source(self, source: Enum) -> "SignatureTemplateCombinationFieldInfoBuilder":
        self._signature_template_combination_field_info.source = source
        return self

    def build(self) -> "SignatureTemplateCombinationFieldInfo":
        return self._signature_template_combination_field_info
