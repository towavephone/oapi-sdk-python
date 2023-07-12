# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n


class OfferApplyFormConfigOptionInfo(object):
    _types = {
        "id": str,
        "name": I18n,
        "description": I18n,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.description: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplyFormConfigOptionInfoBuilder":
        return OfferApplyFormConfigOptionInfoBuilder()


class OfferApplyFormConfigOptionInfoBuilder(object):
    def __init__(self, offer_apply_form_config_option_info: OfferApplyFormConfigOptionInfo = OfferApplyFormConfigOptionInfo({})) -> None:
        self._offer_apply_form_config_option_info: OfferApplyFormConfigOptionInfo = offer_apply_form_config_option_info
    
    def id(self, id: str) -> "OfferApplyFormConfigOptionInfoBuilder":
        self._offer_apply_form_config_option_info.id = id
        return self
    
    def name(self, name: I18n) -> "OfferApplyFormConfigOptionInfoBuilder":
        self._offer_apply_form_config_option_info.name = name
        return self
    
    def description(self, description: I18n) -> "OfferApplyFormConfigOptionInfoBuilder":
        self._offer_apply_form_config_option_info.description = description
        return self
    
    def build(self) -> "OfferApplyFormConfigOptionInfo":
        return self._offer_apply_form_config_option_info