# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetMailgroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.mailgroup_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetMailgroupRequestBuilder":
        return GetMailgroupRequestBuilder()


class GetMailgroupRequestBuilder(object):

    def __init__(self, get_mailgroup_request: GetMailgroupRequest = GetMailgroupRequest()) -> None:
        get_mailgroup_request.http_method = HttpMethod.GET
        get_mailgroup_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id"
        get_mailgroup_request.token_types = {AccessTokenType.TENANT}
        self._get_mailgroup_request: GetMailgroupRequest = get_mailgroup_request
    
    def mailgroup_id(self, mailgroup_id: str) -> "GetMailgroupRequestBuilder":
        self._get_mailgroup_request.mailgroup_id = mailgroup_id
        self._get_mailgroup_request.paths["mailgroup_id"] = mailgroup_id
        return self
    

    def build(self) -> GetMailgroupRequest:
        return self._get_mailgroup_request
