# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .public_mailbox_member import PublicMailboxMember


class BatchCreatePublicMailboxMemberResponseBody(object):
    _types = {
        "items": List[PublicMailboxMember],
    }

    def __init__(self, d):
        self.items: Optional[List[PublicMailboxMember]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreatePublicMailboxMemberResponseBodyBuilder":
        return BatchCreatePublicMailboxMemberResponseBodyBuilder()


class BatchCreatePublicMailboxMemberResponseBodyBuilder(object):
    def __init__(self, batch_create_public_mailbox_member_response_body: BatchCreatePublicMailboxMemberResponseBody = BatchCreatePublicMailboxMemberResponseBody({})) -> None:
        self._batch_create_public_mailbox_member_response_body: BatchCreatePublicMailboxMemberResponseBody = batch_create_public_mailbox_member_response_body
    
    def items(self, items: List[PublicMailboxMember]) -> "BatchCreatePublicMailboxMemberResponseBodyBuilder":
        self._batch_create_public_mailbox_member_response_body.items = items
        return self
    
    def build(self) -> "BatchCreatePublicMailboxMemberResponseBody":
        return self._batch_create_public_mailbox_member_response_body