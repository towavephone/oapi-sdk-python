# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .id_name_object import IdNameObject


class Referral(object):
    _types = {
        "id": str,
        "application_id": str,
        "create_time": int,
        "referral_user_id": str,
        "referral_user": IdNameObject,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.create_time: Optional[int] = None
        self.referral_user_id: Optional[str] = None
        self.referral_user: Optional[IdNameObject] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReferralBuilder":
        return ReferralBuilder()


class ReferralBuilder(object):
    def __init__(self, referral: Referral = Referral({})) -> None:
        self._referral: Referral = referral
    
    def id(self, id: str) -> "ReferralBuilder":
        self._referral.id = id
        return self
    
    def application_id(self, application_id: str) -> "ReferralBuilder":
        self._referral.application_id = application_id
        return self
    
    def create_time(self, create_time: int) -> "ReferralBuilder":
        self._referral.create_time = create_time
        return self
    
    def referral_user_id(self, referral_user_id: str) -> "ReferralBuilder":
        self._referral.referral_user_id = referral_user_id
        return self
    
    def referral_user(self, referral_user: IdNameObject) -> "ReferralBuilder":
        self._referral.referral_user = referral_user
        return self
    
    def build(self) -> "Referral":
        return self._referral