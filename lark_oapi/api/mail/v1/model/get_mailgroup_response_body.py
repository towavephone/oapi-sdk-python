# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class GetMailgroupResponseBody(object):
    _types = {
        "mailgroup_id": str,
        "email": str,
        "name": str,
        "description": str,
        "direct_members_count": str,
        "include_external_member": bool,
        "include_all_company_member": bool,
        "who_can_send_mail": str,
    }

    def __init__(self, d):
        self.mailgroup_id: Optional[str] = None
        self.email: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.direct_members_count: Optional[str] = None
        self.include_external_member: Optional[bool] = None
        self.include_all_company_member: Optional[bool] = None
        self.who_can_send_mail: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetMailgroupResponseBodyBuilder":
        return GetMailgroupResponseBodyBuilder()


class GetMailgroupResponseBodyBuilder(object):
    def __init__(self, get_mailgroup_response_body: GetMailgroupResponseBody = GetMailgroupResponseBody({})) -> None:
        self._get_mailgroup_response_body: GetMailgroupResponseBody = get_mailgroup_response_body
    
    def mailgroup_id(self, mailgroup_id: str) -> "GetMailgroupResponseBodyBuilder":
        self._get_mailgroup_response_body.mailgroup_id = mailgroup_id
        return self
    
    def email(self, email: str) -> "GetMailgroupResponseBodyBuilder":
        self._get_mailgroup_response_body.email = email
        return self
    
    def name(self, name: str) -> "GetMailgroupResponseBodyBuilder":
        self._get_mailgroup_response_body.name = name
        return self
    
    def description(self, description: str) -> "GetMailgroupResponseBodyBuilder":
        self._get_mailgroup_response_body.description = description
        return self
    
    def direct_members_count(self, direct_members_count: str) -> "GetMailgroupResponseBodyBuilder":
        self._get_mailgroup_response_body.direct_members_count = direct_members_count
        return self
    
    def include_external_member(self, include_external_member: bool) -> "GetMailgroupResponseBodyBuilder":
        self._get_mailgroup_response_body.include_external_member = include_external_member
        return self
    
    def include_all_company_member(self, include_all_company_member: bool) -> "GetMailgroupResponseBodyBuilder":
        self._get_mailgroup_response_body.include_all_company_member = include_all_company_member
        return self
    
    def who_can_send_mail(self, who_can_send_mail: str) -> "GetMailgroupResponseBodyBuilder":
        self._get_mailgroup_response_body.who_can_send_mail = who_can_send_mail
        return self
    
    def build(self) -> "GetMailgroupResponseBody":
        return self._get_mailgroup_response_body