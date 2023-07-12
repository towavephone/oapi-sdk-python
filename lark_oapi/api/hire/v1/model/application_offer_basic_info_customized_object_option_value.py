# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ApplicationOfferBasicInfoCustomizedObjectOptionValue(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationOfferBasicInfoCustomizedObjectOptionValueBuilder":
        return ApplicationOfferBasicInfoCustomizedObjectOptionValueBuilder()


class ApplicationOfferBasicInfoCustomizedObjectOptionValueBuilder(object):
    def __init__(self, application_offer_basic_info_customized_object_option_value: ApplicationOfferBasicInfoCustomizedObjectOptionValue = ApplicationOfferBasicInfoCustomizedObjectOptionValue({})) -> None:
        self._application_offer_basic_info_customized_object_option_value: ApplicationOfferBasicInfoCustomizedObjectOptionValue = application_offer_basic_info_customized_object_option_value
    
    def zh_cn(self, zh_cn: str) -> "ApplicationOfferBasicInfoCustomizedObjectOptionValueBuilder":
        self._application_offer_basic_info_customized_object_option_value.zh_cn = zh_cn
        return self
    
    def en_us(self, en_us: str) -> "ApplicationOfferBasicInfoCustomizedObjectOptionValueBuilder":
        self._application_offer_basic_info_customized_object_option_value.en_us = en_us
        return self
    
    def build(self) -> "ApplicationOfferBasicInfoCustomizedObjectOptionValue":
        return self._application_offer_basic_info_customized_object_option_value