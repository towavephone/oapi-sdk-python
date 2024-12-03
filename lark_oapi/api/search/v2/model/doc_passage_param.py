# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DocPassageParam(object):
    _types = {
        "searchable": bool,
        "doc_tokens": List[str],
        "folder_tokens": List[str],
        "obj_ids": List[str],
        "disable_search_link": bool,
        "excluded_obj_ids": List[str],
        "excluded_doc_tokens": List[str],
        "excluded_folder_tokens": List[str],
        "enable_cross_tenant": bool,
        "only_search_public": bool,
    }

    def __init__(self, d=None):
        self.searchable: Optional[bool] = None
        self.doc_tokens: Optional[List[str]] = None
        self.folder_tokens: Optional[List[str]] = None
        self.obj_ids: Optional[List[str]] = None
        self.disable_search_link: Optional[bool] = None
        self.excluded_obj_ids: Optional[List[str]] = None
        self.excluded_doc_tokens: Optional[List[str]] = None
        self.excluded_folder_tokens: Optional[List[str]] = None
        self.enable_cross_tenant: Optional[bool] = None
        self.only_search_public: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocPassageParamBuilder":
        return DocPassageParamBuilder()


class DocPassageParamBuilder(object):
    def __init__(self) -> None:
        self._doc_passage_param = DocPassageParam()

    def searchable(self, searchable: bool) -> "DocPassageParamBuilder":
        self._doc_passage_param.searchable = searchable
        return self

    def doc_tokens(self, doc_tokens: List[str]) -> "DocPassageParamBuilder":
        self._doc_passage_param.doc_tokens = doc_tokens
        return self

    def folder_tokens(self, folder_tokens: List[str]) -> "DocPassageParamBuilder":
        self._doc_passage_param.folder_tokens = folder_tokens
        return self

    def obj_ids(self, obj_ids: List[str]) -> "DocPassageParamBuilder":
        self._doc_passage_param.obj_ids = obj_ids
        return self

    def disable_search_link(self, disable_search_link: bool) -> "DocPassageParamBuilder":
        self._doc_passage_param.disable_search_link = disable_search_link
        return self

    def excluded_obj_ids(self, excluded_obj_ids: List[str]) -> "DocPassageParamBuilder":
        self._doc_passage_param.excluded_obj_ids = excluded_obj_ids
        return self

    def excluded_doc_tokens(self, excluded_doc_tokens: List[str]) -> "DocPassageParamBuilder":
        self._doc_passage_param.excluded_doc_tokens = excluded_doc_tokens
        return self

    def excluded_folder_tokens(self, excluded_folder_tokens: List[str]) -> "DocPassageParamBuilder":
        self._doc_passage_param.excluded_folder_tokens = excluded_folder_tokens
        return self

    def enable_cross_tenant(self, enable_cross_tenant: bool) -> "DocPassageParamBuilder":
        self._doc_passage_param.enable_cross_tenant = enable_cross_tenant
        return self

    def only_search_public(self, only_search_public: bool) -> "DocPassageParamBuilder":
        self._doc_passage_param.only_search_public = only_search_public
        return self

    def build(self) -> "DocPassageParam":
        return self._doc_passage_param
