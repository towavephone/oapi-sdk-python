# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n


class BankBranch(object):
    _types = {
        "bank_branch_id": str,
        "name": List[I18n],
        "bank_branch_name": List[I18n],
        "bank_id": str,
        "code": str,
        "swift_code": str,
        "status": int,
        "bank_branch_code": str,
        "register_place": str,
        "bank_address": str,
        "create_time": str,
        "update_time": str,
    }

    def __init__(self, d=None):
        self.bank_branch_id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.bank_branch_name: Optional[List[I18n]] = None
        self.bank_id: Optional[str] = None
        self.code: Optional[str] = None
        self.swift_code: Optional[str] = None
        self.status: Optional[int] = None
        self.bank_branch_code: Optional[str] = None
        self.register_place: Optional[str] = None
        self.bank_address: Optional[str] = None
        self.create_time: Optional[str] = None
        self.update_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BankBranchBuilder":
        return BankBranchBuilder()


class BankBranchBuilder(object):
    def __init__(self) -> None:
        self._bank_branch = BankBranch()

    def bank_branch_id(self, bank_branch_id: str) -> "BankBranchBuilder":
        self._bank_branch.bank_branch_id = bank_branch_id
        return self

    def name(self, name: List[I18n]) -> "BankBranchBuilder":
        self._bank_branch.name = name
        return self

    def bank_branch_name(self, bank_branch_name: List[I18n]) -> "BankBranchBuilder":
        self._bank_branch.bank_branch_name = bank_branch_name
        return self

    def bank_id(self, bank_id: str) -> "BankBranchBuilder":
        self._bank_branch.bank_id = bank_id
        return self

    def code(self, code: str) -> "BankBranchBuilder":
        self._bank_branch.code = code
        return self

    def swift_code(self, swift_code: str) -> "BankBranchBuilder":
        self._bank_branch.swift_code = swift_code
        return self

    def status(self, status: int) -> "BankBranchBuilder":
        self._bank_branch.status = status
        return self

    def bank_branch_code(self, bank_branch_code: str) -> "BankBranchBuilder":
        self._bank_branch.bank_branch_code = bank_branch_code
        return self

    def register_place(self, register_place: str) -> "BankBranchBuilder":
        self._bank_branch.register_place = register_place
        return self

    def bank_address(self, bank_address: str) -> "BankBranchBuilder":
        self._bank_branch.bank_address = bank_address
        return self

    def create_time(self, create_time: str) -> "BankBranchBuilder":
        self._bank_branch.create_time = create_time
        return self

    def update_time(self, update_time: str) -> "BankBranchBuilder":
        self._bank_branch.update_time = update_time
        return self

    def build(self) -> "BankBranch":
        return self._bank_branch
