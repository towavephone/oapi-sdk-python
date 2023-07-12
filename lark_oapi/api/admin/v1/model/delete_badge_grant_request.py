# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteBadgeGrantRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.badge_id: Optional[str] = None
        self.grant_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteBadgeGrantRequestBuilder":
        return DeleteBadgeGrantRequestBuilder()


class DeleteBadgeGrantRequestBuilder(object):

    def __init__(self, delete_badge_grant_request: DeleteBadgeGrantRequest = DeleteBadgeGrantRequest()) -> None:
        delete_badge_grant_request.http_method = HttpMethod.DELETE
        delete_badge_grant_request.uri = "/open-apis/admin/v1/badges/:badge_id/grants/:grant_id"
        delete_badge_grant_request.token_types = {AccessTokenType.TENANT}
        self._delete_badge_grant_request: DeleteBadgeGrantRequest = delete_badge_grant_request
    
    def badge_id(self, badge_id: str) -> "DeleteBadgeGrantRequestBuilder":
        self._delete_badge_grant_request.badge_id = badge_id
        self._delete_badge_grant_request.paths["badge_id"] = badge_id
        return self
    
    def grant_id(self, grant_id: str) -> "DeleteBadgeGrantRequestBuilder":
        self._delete_badge_grant_request.grant_id = grant_id
        self._delete_badge_grant_request.paths["grant_id"] = grant_id
        return self
    

    def build(self) -> DeleteBadgeGrantRequest:
        return self._delete_badge_grant_request
