# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .feed_group_rule_cond import FeedGroupRuleCond


class FeedGroupRule(object):
    _types = {
        "condition": FeedGroupRuleCond,
        "action": str,
    }

    def __init__(self, d=None):
        self.condition: Optional[FeedGroupRuleCond] = None
        self.action: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FeedGroupRuleBuilder":
        return FeedGroupRuleBuilder()


class FeedGroupRuleBuilder(object):
    def __init__(self) -> None:
        self._feed_group_rule = FeedGroupRule()

    def condition(self, condition: FeedGroupRuleCond) -> "FeedGroupRuleBuilder":
        self._feed_group_rule.condition = condition
        return self

    def action(self, action: str) -> "FeedGroupRuleBuilder":
        self._feed_group_rule.action = action
        return self

    def build(self) -> "FeedGroupRule":
        return self._feed_group_rule
