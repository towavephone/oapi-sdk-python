# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class AppliOfferBasicCustObjOpV(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppliOfferBasicCustObjOpVBuilder":
        return AppliOfferBasicCustObjOpVBuilder()


class AppliOfferBasicCustObjOpVBuilder(object):
    def __init__(self, appli_offer_basic_cust_obj_op_v: AppliOfferBasicCustObjOpV = AppliOfferBasicCustObjOpV({})) -> None:
        self._appli_offer_basic_cust_obj_op_v: AppliOfferBasicCustObjOpV = appli_offer_basic_cust_obj_op_v
    
    def zh_cn(self, zh_cn: str) -> "AppliOfferBasicCustObjOpVBuilder":
        self._appli_offer_basic_cust_obj_op_v.zh_cn = zh_cn
        return self
    
    def en_us(self, en_us: str) -> "AppliOfferBasicCustObjOpVBuilder":
        self._appli_offer_basic_cust_obj_op_v.en_us = en_us
        return self
    
    def build(self) -> "AppliOfferBasicCustObjOpV":
        return self._appli_offer_basic_cust_obj_op_v