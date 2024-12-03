# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FeedGroupRuleCondItem(object):
    _types = {
        "type": str,
        "operator": str,
        "keyword": str,
        "user_id": str,
        "chat_type": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.operator: Optional[str] = None
        self.keyword: Optional[str] = None
        self.user_id: Optional[str] = None
        self.chat_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FeedGroupRuleCondItemBuilder":
        return FeedGroupRuleCondItemBuilder()


class FeedGroupRuleCondItemBuilder(object):
    def __init__(self) -> None:
        self._feed_group_rule_cond_item = FeedGroupRuleCondItem()

    def type(self, type: str) -> "FeedGroupRuleCondItemBuilder":
        self._feed_group_rule_cond_item.type = type
        return self

    def operator(self, operator: str) -> "FeedGroupRuleCondItemBuilder":
        self._feed_group_rule_cond_item.operator = operator
        return self

    def keyword(self, keyword: str) -> "FeedGroupRuleCondItemBuilder":
        self._feed_group_rule_cond_item.keyword = keyword
        return self

    def user_id(self, user_id: str) -> "FeedGroupRuleCondItemBuilder":
        self._feed_group_rule_cond_item.user_id = user_id
        return self

    def chat_type(self, chat_type: str) -> "FeedGroupRuleCondItemBuilder":
        self._feed_group_rule_cond_item.chat_type = chat_type
        return self

    def build(self) -> "FeedGroupRuleCondItem":
        return self._feed_group_rule_cond_item
