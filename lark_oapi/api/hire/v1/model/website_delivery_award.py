# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .website_delivery_customized_data import WebsiteDeliveryCustomizedData


class WebsiteDeliveryAward(object):
    _types = {
        "customized_data": List[WebsiteDeliveryCustomizedData],
        "desc": str,
        "title": str,
        "award_time": int,
    }

    def __init__(self, d):
        self.customized_data: Optional[List[WebsiteDeliveryCustomizedData]] = None
        self.desc: Optional[str] = None
        self.title: Optional[str] = None
        self.award_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliveryAwardBuilder":
        return WebsiteDeliveryAwardBuilder()


class WebsiteDeliveryAwardBuilder(object):
    def __init__(self, website_delivery_award: WebsiteDeliveryAward = WebsiteDeliveryAward({})) -> None:
        self._website_delivery_award: WebsiteDeliveryAward = website_delivery_award
    
    def customized_data(self, customized_data: List[WebsiteDeliveryCustomizedData]) -> "WebsiteDeliveryAwardBuilder":
        self._website_delivery_award.customized_data = customized_data
        return self
    
    def desc(self, desc: str) -> "WebsiteDeliveryAwardBuilder":
        self._website_delivery_award.desc = desc
        return self
    
    def title(self, title: str) -> "WebsiteDeliveryAwardBuilder":
        self._website_delivery_award.title = title
        return self
    
    def award_time(self, award_time: int) -> "WebsiteDeliveryAwardBuilder":
        self._website_delivery_award.award_time = award_time
        return self
    
    def build(self) -> "WebsiteDeliveryAward":
        return self._website_delivery_award