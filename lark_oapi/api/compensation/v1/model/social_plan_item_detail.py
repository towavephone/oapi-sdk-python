# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .social_plan_item_setting import SocialPlanItemSetting
from .social_plan_item_setting import SocialPlanItemSetting


class SocialPlanItemDetail(object):
    _types = {
        "item_id": str,
        "item_name": I18n,
        "item_setting_of_person": SocialPlanItemSetting,
        "item_setting_of_company": SocialPlanItemSetting,
        "payment_frequency": str,
        "payment_months": List[int],
    }

    def __init__(self, d=None):
        self.item_id: Optional[str] = None
        self.item_name: Optional[I18n] = None
        self.item_setting_of_person: Optional[SocialPlanItemSetting] = None
        self.item_setting_of_company: Optional[SocialPlanItemSetting] = None
        self.payment_frequency: Optional[str] = None
        self.payment_months: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SocialPlanItemDetailBuilder":
        return SocialPlanItemDetailBuilder()


class SocialPlanItemDetailBuilder(object):
    def __init__(self) -> None:
        self._social_plan_item_detail = SocialPlanItemDetail()

    def item_id(self, item_id: str) -> "SocialPlanItemDetailBuilder":
        self._social_plan_item_detail.item_id = item_id
        return self

    def item_name(self, item_name: I18n) -> "SocialPlanItemDetailBuilder":
        self._social_plan_item_detail.item_name = item_name
        return self

    def item_setting_of_person(self, item_setting_of_person: SocialPlanItemSetting) -> "SocialPlanItemDetailBuilder":
        self._social_plan_item_detail.item_setting_of_person = item_setting_of_person
        return self

    def item_setting_of_company(self, item_setting_of_company: SocialPlanItemSetting) -> "SocialPlanItemDetailBuilder":
        self._social_plan_item_detail.item_setting_of_company = item_setting_of_company
        return self

    def payment_frequency(self, payment_frequency: str) -> "SocialPlanItemDetailBuilder":
        self._social_plan_item_detail.payment_frequency = payment_frequency
        return self

    def payment_months(self, payment_months: List[int]) -> "SocialPlanItemDetailBuilder":
        self._social_plan_item_detail.payment_months = payment_months
        return self

    def build(self) -> "SocialPlanItemDetail":
        return self._social_plan_item_detail
