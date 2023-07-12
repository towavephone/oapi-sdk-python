# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .company import Company


class GetCompanyResponseBody(object):
    _types = {
        "company": Company,
    }

    def __init__(self, d):
        self.company: Optional[Company] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetCompanyResponseBodyBuilder":
        return GetCompanyResponseBodyBuilder()


class GetCompanyResponseBodyBuilder(object):
    def __init__(self, get_company_response_body: GetCompanyResponseBody = GetCompanyResponseBody({})) -> None:
        self._get_company_response_body: GetCompanyResponseBody = get_company_response_body
    
    def company(self, company: Company) -> "GetCompanyResponseBodyBuilder":
        self._get_company_response_body.company = company
        return self
    
    def build(self) -> "GetCompanyResponseBody":
        return self._get_company_response_body