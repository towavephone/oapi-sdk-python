# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .update_talent_external_info_request_body import UpdateTalentExternalInfoRequestBody


class UpdateTalentExternalInfoRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.talent_id: Optional[str] = None
        self.request_body: Optional[UpdateTalentExternalInfoRequestBody] = None

    @staticmethod
    def builder() -> "UpdateTalentExternalInfoRequestBuilder":
        return UpdateTalentExternalInfoRequestBuilder()


class UpdateTalentExternalInfoRequestBuilder(object):

    def __init__(self) -> None:
        update_talent_external_info_request = UpdateTalentExternalInfoRequest()
        update_talent_external_info_request.http_method = HttpMethod.PUT
        update_talent_external_info_request.uri = "/open-apis/hire/v1/talents/:talent_id/external_info"
        update_talent_external_info_request.token_types = {AccessTokenType.TENANT}
        self._update_talent_external_info_request: UpdateTalentExternalInfoRequest = update_talent_external_info_request

    def talent_id(self, talent_id: str) -> "UpdateTalentExternalInfoRequestBuilder":
        self._update_talent_external_info_request.talent_id = talent_id
        self._update_talent_external_info_request.paths["talent_id"] = str(talent_id)
        return self

    def request_body(self,
                     request_body: UpdateTalentExternalInfoRequestBody) -> "UpdateTalentExternalInfoRequestBuilder":
        self._update_talent_external_info_request.request_body = request_body
        self._update_talent_external_info_request.body = request_body
        return self

    def build(self) -> UpdateTalentExternalInfoRequest:
        return self._update_talent_external_info_request
