# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ApplicationOfferOnboardProfileCity(object):
    _types = {
        "code": str,
        "name": str,
        "en_name": str,
        "location_type": int,
    }

    def __init__(self, d):
        self.code: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.location_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationOfferOnboardProfileCityBuilder":
        return ApplicationOfferOnboardProfileCityBuilder()


class ApplicationOfferOnboardProfileCityBuilder(object):
    def __init__(self, application_offer_onboard_profile_city: ApplicationOfferOnboardProfileCity = ApplicationOfferOnboardProfileCity({})) -> None:
        self._application_offer_onboard_profile_city: ApplicationOfferOnboardProfileCity = application_offer_onboard_profile_city
    
    def code(self, code: str) -> "ApplicationOfferOnboardProfileCityBuilder":
        self._application_offer_onboard_profile_city.code = code
        return self
    
    def name(self, name: str) -> "ApplicationOfferOnboardProfileCityBuilder":
        self._application_offer_onboard_profile_city.name = name
        return self
    
    def en_name(self, en_name: str) -> "ApplicationOfferOnboardProfileCityBuilder":
        self._application_offer_onboard_profile_city.en_name = en_name
        return self
    
    def location_type(self, location_type: int) -> "ApplicationOfferOnboardProfileCityBuilder":
        self._application_offer_onboard_profile_city.location_type = location_type
        return self
    
    def build(self) -> "ApplicationOfferOnboardProfileCity":
        return self._application_offer_onboard_profile_city