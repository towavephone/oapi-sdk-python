# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class LumpSumPaymentDetailForUpdate(object):
    _types = {
        "id": str,
        "issuance_amount": str,
        "issuance_status": str,
        "issuance_way": str,
        "issuance_time": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.issuance_amount: Optional[str] = None
        self.issuance_status: Optional[str] = None
        self.issuance_way: Optional[str] = None
        self.issuance_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LumpSumPaymentDetailForUpdateBuilder":
        return LumpSumPaymentDetailForUpdateBuilder()


class LumpSumPaymentDetailForUpdateBuilder(object):
    def __init__(self) -> None:
        self._lump_sum_payment_detail_for_update = LumpSumPaymentDetailForUpdate()

    def id(self, id: str) -> "LumpSumPaymentDetailForUpdateBuilder":
        self._lump_sum_payment_detail_for_update.id = id
        return self

    def issuance_amount(self, issuance_amount: str) -> "LumpSumPaymentDetailForUpdateBuilder":
        self._lump_sum_payment_detail_for_update.issuance_amount = issuance_amount
        return self

    def issuance_status(self, issuance_status: str) -> "LumpSumPaymentDetailForUpdateBuilder":
        self._lump_sum_payment_detail_for_update.issuance_status = issuance_status
        return self

    def issuance_way(self, issuance_way: str) -> "LumpSumPaymentDetailForUpdateBuilder":
        self._lump_sum_payment_detail_for_update.issuance_way = issuance_way
        return self

    def issuance_time(self, issuance_time: str) -> "LumpSumPaymentDetailForUpdateBuilder":
        self._lump_sum_payment_detail_for_update.issuance_time = issuance_time
        return self

    def build(self) -> "LumpSumPaymentDetailForUpdate":
        return self._lump_sum_payment_detail_for_update
