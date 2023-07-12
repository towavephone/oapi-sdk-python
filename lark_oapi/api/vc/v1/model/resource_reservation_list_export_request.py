# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .resource_reservation_list_export_request_body import ResourceReservationListExportRequestBody


class ResourceReservationListExportRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ResourceReservationListExportRequestBody] = None

    @staticmethod
    def builder() -> "ResourceReservationListExportRequestBuilder":
        return ResourceReservationListExportRequestBuilder()


class ResourceReservationListExportRequestBuilder(object):

    def __init__(self, resource_reservation_list_export_request: ResourceReservationListExportRequest = ResourceReservationListExportRequest()) -> None:
        resource_reservation_list_export_request.http_method = HttpMethod.POST
        resource_reservation_list_export_request.uri = "/open-apis/vc/v1/exports/resource_reservation_list"
        resource_reservation_list_export_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._resource_reservation_list_export_request: ResourceReservationListExportRequest = resource_reservation_list_export_request
    
    def request_body(self, request_body: ResourceReservationListExportRequestBody) -> "ResourceReservationListExportRequestBuilder":
        self._resource_reservation_list_export_request.request_body = request_body
        self._resource_reservation_list_export_request.body = request_body
        return self

    def build(self) -> ResourceReservationListExportRequest:
        return self._resource_reservation_list_export_request
