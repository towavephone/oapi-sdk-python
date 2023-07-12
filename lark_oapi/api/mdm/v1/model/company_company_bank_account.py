# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .i18n_struct import I18nStruct


class CompanyCompanyBankAccount(object):
    _types = {
        "company_bank_account_uid": str,
        "company_uid": str,
        "account": str,
        "iban": str,
        "account_name": str,
        "currency_code": str,
        "local_routing_code": str,
        "gl_account_code": str,
        "clearing_account_code": str,
        "swift": str,
        "account_attri_desc": str,
        "i18n_account_attri_desc": List[I18nStruct],
    }

    def __init__(self, d):
        self.company_bank_account_uid: Optional[str] = None
        self.company_uid: Optional[str] = None
        self.account: Optional[str] = None
        self.iban: Optional[str] = None
        self.account_name: Optional[str] = None
        self.currency_code: Optional[str] = None
        self.local_routing_code: Optional[str] = None
        self.gl_account_code: Optional[str] = None
        self.clearing_account_code: Optional[str] = None
        self.swift: Optional[str] = None
        self.account_attri_desc: Optional[str] = None
        self.i18n_account_attri_desc: Optional[List[I18nStruct]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CompanyCompanyBankAccountBuilder":
        return CompanyCompanyBankAccountBuilder()


class CompanyCompanyBankAccountBuilder(object):
    def __init__(self, company_company_bank_account: CompanyCompanyBankAccount = CompanyCompanyBankAccount({})) -> None:
        self._company_company_bank_account: CompanyCompanyBankAccount = company_company_bank_account
    
    def company_bank_account_uid(self, company_bank_account_uid: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.company_bank_account_uid = company_bank_account_uid
        return self
    
    def company_uid(self, company_uid: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.company_uid = company_uid
        return self
    
    def account(self, account: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.account = account
        return self
    
    def iban(self, iban: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.iban = iban
        return self
    
    def account_name(self, account_name: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.account_name = account_name
        return self
    
    def currency_code(self, currency_code: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.currency_code = currency_code
        return self
    
    def local_routing_code(self, local_routing_code: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.local_routing_code = local_routing_code
        return self
    
    def gl_account_code(self, gl_account_code: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.gl_account_code = gl_account_code
        return self
    
    def clearing_account_code(self, clearing_account_code: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.clearing_account_code = clearing_account_code
        return self
    
    def swift(self, swift: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.swift = swift
        return self
    
    def account_attri_desc(self, account_attri_desc: str) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.account_attri_desc = account_attri_desc
        return self
    
    def i18n_account_attri_desc(self, i18n_account_attri_desc: List[I18nStruct]) -> "CompanyCompanyBankAccountBuilder":
        self._company_company_bank_account.i18n_account_attri_desc = i18n_account_attri_desc
        return self
    
    def build(self) -> "CompanyCompanyBankAccount":
        return self._company_company_bank_account