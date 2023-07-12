# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .offer_status_offer_request_body import OfferStatusOfferRequestBody


class OfferStatusOfferRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.offer_id: Optional[str] = None
        self.request_body: Optional[OfferStatusOfferRequestBody] = None

    @staticmethod
    def builder() -> "OfferStatusOfferRequestBuilder":
        return OfferStatusOfferRequestBuilder()


class OfferStatusOfferRequestBuilder(object):

    def __init__(self, offer_status_offer_request: OfferStatusOfferRequest = OfferStatusOfferRequest()) -> None:
        offer_status_offer_request.http_method = HttpMethod.PATCH
        offer_status_offer_request.uri = "/open-apis/hire/v1/offers/:offer_id/offer_status"
        offer_status_offer_request.token_types = {AccessTokenType.TENANT}
        self._offer_status_offer_request: OfferStatusOfferRequest = offer_status_offer_request
    
    def offer_id(self, offer_id: str) -> "OfferStatusOfferRequestBuilder":
        self._offer_status_offer_request.offer_id = offer_id
        self._offer_status_offer_request.paths["offer_id"] = offer_id
        return self
    
    def request_body(self, request_body: OfferStatusOfferRequestBody) -> "OfferStatusOfferRequestBuilder":
        self._offer_status_offer_request.request_body = request_body
        self._offer_status_offer_request.body = request_body
        return self

    def build(self) -> OfferStatusOfferRequest:
        return self._offer_status_offer_request
