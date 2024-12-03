# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .location_address_create import LocationAddressCreate


class CreateLocationAddressRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.location_id: Optional[str] = None
        self.request_body: Optional[LocationAddressCreate] = None

    @staticmethod
    def builder() -> "CreateLocationAddressRequestBuilder":
        return CreateLocationAddressRequestBuilder()


class CreateLocationAddressRequestBuilder(object):

    def __init__(self) -> None:
        create_location_address_request = CreateLocationAddressRequest()
        create_location_address_request.http_method = HttpMethod.POST
        create_location_address_request.uri = "/open-apis/corehr/v2/locations/:location_id/addresses"
        create_location_address_request.token_types = {AccessTokenType.TENANT}
        self._create_location_address_request: CreateLocationAddressRequest = create_location_address_request

    def client_token(self, client_token: str) -> "CreateLocationAddressRequestBuilder":
        self._create_location_address_request.client_token = client_token
        self._create_location_address_request.add_query("client_token", client_token)
        return self

    def location_id(self, location_id: str) -> "CreateLocationAddressRequestBuilder":
        self._create_location_address_request.location_id = location_id
        self._create_location_address_request.paths["location_id"] = str(location_id)
        return self

    def request_body(self, request_body: LocationAddressCreate) -> "CreateLocationAddressRequestBuilder":
        self._create_location_address_request.request_body = request_body
        self._create_location_address_request.body = request_body
        return self

    def build(self) -> CreateLocationAddressRequest:
        return self._create_location_address_request
