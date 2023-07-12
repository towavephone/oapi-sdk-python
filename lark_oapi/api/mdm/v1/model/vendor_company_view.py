# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .extend_field import ExtendField


class VendorCompanyView(object):
    _types = {
        "id": int,
        "company_code": str,
        "gl_account": str,
        "vendor_site_code": str,
        "payment_term": str,
        "down_payment_term": str,
        "extend_info": List[ExtendField],
    }

    def __init__(self, d):
        self.id: Optional[int] = None
        self.company_code: Optional[str] = None
        self.gl_account: Optional[str] = None
        self.vendor_site_code: Optional[str] = None
        self.payment_term: Optional[str] = None
        self.down_payment_term: Optional[str] = None
        self.extend_info: Optional[List[ExtendField]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "VendorCompanyViewBuilder":
        return VendorCompanyViewBuilder()


class VendorCompanyViewBuilder(object):
    def __init__(self, vendor_company_view: VendorCompanyView = VendorCompanyView({})) -> None:
        self._vendor_company_view: VendorCompanyView = vendor_company_view
    
    def id(self, id: int) -> "VendorCompanyViewBuilder":
        self._vendor_company_view.id = id
        return self
    
    def company_code(self, company_code: str) -> "VendorCompanyViewBuilder":
        self._vendor_company_view.company_code = company_code
        return self
    
    def gl_account(self, gl_account: str) -> "VendorCompanyViewBuilder":
        self._vendor_company_view.gl_account = gl_account
        return self
    
    def vendor_site_code(self, vendor_site_code: str) -> "VendorCompanyViewBuilder":
        self._vendor_company_view.vendor_site_code = vendor_site_code
        return self
    
    def payment_term(self, payment_term: str) -> "VendorCompanyViewBuilder":
        self._vendor_company_view.payment_term = payment_term
        return self
    
    def down_payment_term(self, down_payment_term: str) -> "VendorCompanyViewBuilder":
        self._vendor_company_view.down_payment_term = down_payment_term
        return self
    
    def extend_info(self, extend_info: List[ExtendField]) -> "VendorCompanyViewBuilder":
        self._vendor_company_view.extend_info = extend_info
        return self
    
    def build(self) -> "VendorCompanyView":
        return self._vendor_company_view