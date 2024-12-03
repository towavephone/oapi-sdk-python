# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .external_common_attachment import ExternalCommonAttachment


class ExternalOffer(object):
    _types = {
        "id": str,
        "external_id": str,
        "external_application_id": str,
        "biz_create_time": str,
        "owner": str,
        "offer_status": str,
        "attachment_id_list": List[str],
        "attachment_list": List[ExternalCommonAttachment],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.external_id: Optional[str] = None
        self.external_application_id: Optional[str] = None
        self.biz_create_time: Optional[str] = None
        self.owner: Optional[str] = None
        self.offer_status: Optional[str] = None
        self.attachment_id_list: Optional[List[str]] = None
        self.attachment_list: Optional[List[ExternalCommonAttachment]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalOfferBuilder":
        return ExternalOfferBuilder()


class ExternalOfferBuilder(object):
    def __init__(self) -> None:
        self._external_offer = ExternalOffer()

    def id(self, id: str) -> "ExternalOfferBuilder":
        self._external_offer.id = id
        return self

    def external_id(self, external_id: str) -> "ExternalOfferBuilder":
        self._external_offer.external_id = external_id
        return self

    def external_application_id(self, external_application_id: str) -> "ExternalOfferBuilder":
        self._external_offer.external_application_id = external_application_id
        return self

    def biz_create_time(self, biz_create_time: str) -> "ExternalOfferBuilder":
        self._external_offer.biz_create_time = biz_create_time
        return self

    def owner(self, owner: str) -> "ExternalOfferBuilder":
        self._external_offer.owner = owner
        return self

    def offer_status(self, offer_status: str) -> "ExternalOfferBuilder":
        self._external_offer.offer_status = offer_status
        return self

    def attachment_id_list(self, attachment_id_list: List[str]) -> "ExternalOfferBuilder":
        self._external_offer.attachment_id_list = attachment_id_list
        return self

    def attachment_list(self, attachment_list: List[ExternalCommonAttachment]) -> "ExternalOfferBuilder":
        self._external_offer.attachment_list = attachment_list
        return self

    def build(self) -> "ExternalOffer":
        return self._external_offer
