# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class OnboardingFlowChange(object):
    _types = {
        "after_status": str,
    }

    def __init__(self, d=None):
        self.after_status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OnboardingFlowChangeBuilder":
        return OnboardingFlowChangeBuilder()


class OnboardingFlowChangeBuilder(object):
    def __init__(self) -> None:
        self._onboarding_flow_change = OnboardingFlowChange()

    def after_status(self, after_status: str) -> "OnboardingFlowChangeBuilder":
        self._onboarding_flow_change.after_status = after_status
        return self

    def build(self) -> "OnboardingFlowChange":
        return self._onboarding_flow_change
