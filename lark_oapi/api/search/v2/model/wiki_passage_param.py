# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class WikiPassageParam(object):
    _types = {
        "searchable": bool,
        "space_ids": List[str],
        "obj_ids": List[str],
        "wiki_tokens": List[str],
        "node_tokens": List[str],
        "excluded_space_ids": List[str],
        "excluded_obj_ids": List[str],
        "excluded_wiki_tokens": List[str],
        "excluded_node_tokens": List[str],
        "enable_cross_tenant": bool,
        "only_search_public": bool,
    }

    def __init__(self, d=None):
        self.searchable: Optional[bool] = None
        self.space_ids: Optional[List[str]] = None
        self.obj_ids: Optional[List[str]] = None
        self.wiki_tokens: Optional[List[str]] = None
        self.node_tokens: Optional[List[str]] = None
        self.excluded_space_ids: Optional[List[str]] = None
        self.excluded_obj_ids: Optional[List[str]] = None
        self.excluded_wiki_tokens: Optional[List[str]] = None
        self.excluded_node_tokens: Optional[List[str]] = None
        self.enable_cross_tenant: Optional[bool] = None
        self.only_search_public: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WikiPassageParamBuilder":
        return WikiPassageParamBuilder()


class WikiPassageParamBuilder(object):
    def __init__(self) -> None:
        self._wiki_passage_param = WikiPassageParam()

    def searchable(self, searchable: bool) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.searchable = searchable
        return self

    def space_ids(self, space_ids: List[str]) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.space_ids = space_ids
        return self

    def obj_ids(self, obj_ids: List[str]) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.obj_ids = obj_ids
        return self

    def wiki_tokens(self, wiki_tokens: List[str]) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.wiki_tokens = wiki_tokens
        return self

    def node_tokens(self, node_tokens: List[str]) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.node_tokens = node_tokens
        return self

    def excluded_space_ids(self, excluded_space_ids: List[str]) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.excluded_space_ids = excluded_space_ids
        return self

    def excluded_obj_ids(self, excluded_obj_ids: List[str]) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.excluded_obj_ids = excluded_obj_ids
        return self

    def excluded_wiki_tokens(self, excluded_wiki_tokens: List[str]) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.excluded_wiki_tokens = excluded_wiki_tokens
        return self

    def excluded_node_tokens(self, excluded_node_tokens: List[str]) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.excluded_node_tokens = excluded_node_tokens
        return self

    def enable_cross_tenant(self, enable_cross_tenant: bool) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.enable_cross_tenant = enable_cross_tenant
        return self

    def only_search_public(self, only_search_public: bool) -> "WikiPassageParamBuilder":
        self._wiki_passage_param.only_search_public = only_search_public
        return self

    def build(self) -> "WikiPassageParam":
        return self._wiki_passage_param
