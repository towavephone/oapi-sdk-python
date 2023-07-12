# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class UpdatePublicMailboxResponseBody(object):
    _types = {
        "public_mailbox_id": str,
        "email": str,
        "name": str,
    }

    def __init__(self, d):
        self.public_mailbox_id: Optional[str] = None
        self.email: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdatePublicMailboxResponseBodyBuilder":
        return UpdatePublicMailboxResponseBodyBuilder()


class UpdatePublicMailboxResponseBodyBuilder(object):
    def __init__(self, update_public_mailbox_response_body: UpdatePublicMailboxResponseBody = UpdatePublicMailboxResponseBody({})) -> None:
        self._update_public_mailbox_response_body: UpdatePublicMailboxResponseBody = update_public_mailbox_response_body
    
    def public_mailbox_id(self, public_mailbox_id: str) -> "UpdatePublicMailboxResponseBodyBuilder":
        self._update_public_mailbox_response_body.public_mailbox_id = public_mailbox_id
        return self
    
    def email(self, email: str) -> "UpdatePublicMailboxResponseBodyBuilder":
        self._update_public_mailbox_response_body.email = email
        return self
    
    def name(self, name: str) -> "UpdatePublicMailboxResponseBodyBuilder":
        self._update_public_mailbox_response_body.name = name
        return self
    
    def build(self) -> "UpdatePublicMailboxResponseBody":
        return self._update_public_mailbox_response_body