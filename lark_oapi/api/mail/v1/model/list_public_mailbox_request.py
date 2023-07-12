# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListPublicMailboxRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListPublicMailboxRequestBuilder":
        return ListPublicMailboxRequestBuilder()


class ListPublicMailboxRequestBuilder(object):

    def __init__(self, list_public_mailbox_request: ListPublicMailboxRequest = ListPublicMailboxRequest()) -> None:
        list_public_mailbox_request.http_method = HttpMethod.GET
        list_public_mailbox_request.uri = "/open-apis/mail/v1/public_mailboxes"
        list_public_mailbox_request.token_types = {AccessTokenType.TENANT}
        self._list_public_mailbox_request: ListPublicMailboxRequest = list_public_mailbox_request
    
    def page_token(self, page_token: str) -> "ListPublicMailboxRequestBuilder":
        self._list_public_mailbox_request.page_token = page_token
        self._list_public_mailbox_request.queries["page_token"] = str(page_token)
        return self
    
    def page_size(self, page_size: int) -> "ListPublicMailboxRequestBuilder":
        self._list_public_mailbox_request.page_size = page_size
        self._list_public_mailbox_request.queries["page_size"] = str(page_size)
        return self
    

    def build(self) -> ListPublicMailboxRequest:
        return self._list_public_mailbox_request
