# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .extend_field import ExtendField
from .vendor_account import VendorAccount
from .vendor_address import VendorAddress
from .vendor_company_view import VendorCompanyView
from .vendor_contact import VendorContact
from .appendix import Appendix


class Vendor(object):
    _types = {
        "id": int,
        "ad_country": str,
        "ad_province": str,
        "ad_city": str,
        "address": str,
        "ad_postcode": str,
        "legal_person": str,
        "certification_type": str,
        "certification_id": str,
        "contact_person": str,
        "contact_telephone": str,
        "contact_mobile_phone": str,
        "fax": str,
        "e_mail": str,
        "status": int,
        "vendor": str,
        "vendor_text": str,
        "short_text": str,
        "vendor_type": str,
        "vendor_category": str,
        "vendor_nature": str,
        "linked_employee": str,
        "linked_customer": str,
        "associated_with_legal_entity": bool,
        "extend_info": List[ExtendField],
        "vendor_accounts": List[VendorAccount],
        "vendor_addresses": List[VendorAddress],
        "vendor_company_views": List[VendorCompanyView],
        "vendor_contacts": List[VendorContact],
        "gl_account": str,
        "down_payment_term": str,
        "payment_term": str,
        "vendor_site_code": str,
        "appendix": List[Appendix],
        "is_risked": bool,
        "owner_depts": List[str],
    }

    def __init__(self, d):
        self.id: Optional[int] = None
        self.ad_country: Optional[str] = None
        self.ad_province: Optional[str] = None
        self.ad_city: Optional[str] = None
        self.address: Optional[str] = None
        self.ad_postcode: Optional[str] = None
        self.legal_person: Optional[str] = None
        self.certification_type: Optional[str] = None
        self.certification_id: Optional[str] = None
        self.contact_person: Optional[str] = None
        self.contact_telephone: Optional[str] = None
        self.contact_mobile_phone: Optional[str] = None
        self.fax: Optional[str] = None
        self.e_mail: Optional[str] = None
        self.status: Optional[int] = None
        self.vendor: Optional[str] = None
        self.vendor_text: Optional[str] = None
        self.short_text: Optional[str] = None
        self.vendor_type: Optional[str] = None
        self.vendor_category: Optional[str] = None
        self.vendor_nature: Optional[str] = None
        self.linked_employee: Optional[str] = None
        self.linked_customer: Optional[str] = None
        self.associated_with_legal_entity: Optional[bool] = None
        self.extend_info: Optional[List[ExtendField]] = None
        self.vendor_accounts: Optional[List[VendorAccount]] = None
        self.vendor_addresses: Optional[List[VendorAddress]] = None
        self.vendor_company_views: Optional[List[VendorCompanyView]] = None
        self.vendor_contacts: Optional[List[VendorContact]] = None
        self.gl_account: Optional[str] = None
        self.down_payment_term: Optional[str] = None
        self.payment_term: Optional[str] = None
        self.vendor_site_code: Optional[str] = None
        self.appendix: Optional[List[Appendix]] = None
        self.is_risked: Optional[bool] = None
        self.owner_depts: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "VendorBuilder":
        return VendorBuilder()


class VendorBuilder(object):
    def __init__(self, vendor: Vendor = Vendor({})) -> None:
        self._vendor: Vendor = vendor
    
    def id(self, id: int) -> "VendorBuilder":
        self._vendor.id = id
        return self
    
    def ad_country(self, ad_country: str) -> "VendorBuilder":
        self._vendor.ad_country = ad_country
        return self
    
    def ad_province(self, ad_province: str) -> "VendorBuilder":
        self._vendor.ad_province = ad_province
        return self
    
    def ad_city(self, ad_city: str) -> "VendorBuilder":
        self._vendor.ad_city = ad_city
        return self
    
    def address(self, address: str) -> "VendorBuilder":
        self._vendor.address = address
        return self
    
    def ad_postcode(self, ad_postcode: str) -> "VendorBuilder":
        self._vendor.ad_postcode = ad_postcode
        return self
    
    def legal_person(self, legal_person: str) -> "VendorBuilder":
        self._vendor.legal_person = legal_person
        return self
    
    def certification_type(self, certification_type: str) -> "VendorBuilder":
        self._vendor.certification_type = certification_type
        return self
    
    def certification_id(self, certification_id: str) -> "VendorBuilder":
        self._vendor.certification_id = certification_id
        return self
    
    def contact_person(self, contact_person: str) -> "VendorBuilder":
        self._vendor.contact_person = contact_person
        return self
    
    def contact_telephone(self, contact_telephone: str) -> "VendorBuilder":
        self._vendor.contact_telephone = contact_telephone
        return self
    
    def contact_mobile_phone(self, contact_mobile_phone: str) -> "VendorBuilder":
        self._vendor.contact_mobile_phone = contact_mobile_phone
        return self
    
    def fax(self, fax: str) -> "VendorBuilder":
        self._vendor.fax = fax
        return self
    
    def e_mail(self, e_mail: str) -> "VendorBuilder":
        self._vendor.e_mail = e_mail
        return self
    
    def status(self, status: int) -> "VendorBuilder":
        self._vendor.status = status
        return self
    
    def vendor(self, vendor: str) -> "VendorBuilder":
        self._vendor.vendor = vendor
        return self
    
    def vendor_text(self, vendor_text: str) -> "VendorBuilder":
        self._vendor.vendor_text = vendor_text
        return self
    
    def short_text(self, short_text: str) -> "VendorBuilder":
        self._vendor.short_text = short_text
        return self
    
    def vendor_type(self, vendor_type: str) -> "VendorBuilder":
        self._vendor.vendor_type = vendor_type
        return self
    
    def vendor_category(self, vendor_category: str) -> "VendorBuilder":
        self._vendor.vendor_category = vendor_category
        return self
    
    def vendor_nature(self, vendor_nature: str) -> "VendorBuilder":
        self._vendor.vendor_nature = vendor_nature
        return self
    
    def linked_employee(self, linked_employee: str) -> "VendorBuilder":
        self._vendor.linked_employee = linked_employee
        return self
    
    def linked_customer(self, linked_customer: str) -> "VendorBuilder":
        self._vendor.linked_customer = linked_customer
        return self
    
    def associated_with_legal_entity(self, associated_with_legal_entity: bool) -> "VendorBuilder":
        self._vendor.associated_with_legal_entity = associated_with_legal_entity
        return self
    
    def extend_info(self, extend_info: List[ExtendField]) -> "VendorBuilder":
        self._vendor.extend_info = extend_info
        return self
    
    def vendor_accounts(self, vendor_accounts: List[VendorAccount]) -> "VendorBuilder":
        self._vendor.vendor_accounts = vendor_accounts
        return self
    
    def vendor_addresses(self, vendor_addresses: List[VendorAddress]) -> "VendorBuilder":
        self._vendor.vendor_addresses = vendor_addresses
        return self
    
    def vendor_company_views(self, vendor_company_views: List[VendorCompanyView]) -> "VendorBuilder":
        self._vendor.vendor_company_views = vendor_company_views
        return self
    
    def vendor_contacts(self, vendor_contacts: List[VendorContact]) -> "VendorBuilder":
        self._vendor.vendor_contacts = vendor_contacts
        return self
    
    def gl_account(self, gl_account: str) -> "VendorBuilder":
        self._vendor.gl_account = gl_account
        return self
    
    def down_payment_term(self, down_payment_term: str) -> "VendorBuilder":
        self._vendor.down_payment_term = down_payment_term
        return self
    
    def payment_term(self, payment_term: str) -> "VendorBuilder":
        self._vendor.payment_term = payment_term
        return self
    
    def vendor_site_code(self, vendor_site_code: str) -> "VendorBuilder":
        self._vendor.vendor_site_code = vendor_site_code
        return self
    
    def appendix(self, appendix: List[Appendix]) -> "VendorBuilder":
        self._vendor.appendix = appendix
        return self
    
    def is_risked(self, is_risked: bool) -> "VendorBuilder":
        self._vendor.is_risked = is_risked
        return self
    
    def owner_depts(self, owner_depts: List[str]) -> "VendorBuilder":
        self._vendor.owner_depts = owner_depts
        return self
    
    def build(self) -> "Vendor":
        return self._vendor