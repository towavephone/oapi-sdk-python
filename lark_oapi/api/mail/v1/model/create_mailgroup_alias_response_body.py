# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .email_alias import EmailAlias


class CreateMailgroupAliasResponseBody(object):
    _types = {
        "mailgroup_alias": EmailAlias,
    }

    def __init__(self, d):
        self.mailgroup_alias: Optional[EmailAlias] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateMailgroupAliasResponseBodyBuilder":
        return CreateMailgroupAliasResponseBodyBuilder()


class CreateMailgroupAliasResponseBodyBuilder(object):
    def __init__(self, create_mailgroup_alias_response_body: CreateMailgroupAliasResponseBody = CreateMailgroupAliasResponseBody({})) -> None:
        self._create_mailgroup_alias_response_body: CreateMailgroupAliasResponseBody = create_mailgroup_alias_response_body
    
    def mailgroup_alias(self, mailgroup_alias: EmailAlias) -> "CreateMailgroupAliasResponseBodyBuilder":
        self._create_mailgroup_alias_response_body.mailgroup_alias = mailgroup_alias
        return self
    
    def build(self) -> "CreateMailgroupAliasResponseBody":
        return self._create_mailgroup_alias_response_body