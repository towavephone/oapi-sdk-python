# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class RecurringPaymentForCreate(object):
    _types = {
        "unique_id": str,
        "user_id": str,
        "item_id": str,
        "each_amount": str,
        "start_date": str,
        "end_date": str,
        "currency_id": str,
        "issuance_type": str,
        "issuance_period": str,
        "remark": str,
    }

    def __init__(self, d=None):
        self.unique_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.item_id: Optional[str] = None
        self.each_amount: Optional[str] = None
        self.start_date: Optional[str] = None
        self.end_date: Optional[str] = None
        self.currency_id: Optional[str] = None
        self.issuance_type: Optional[str] = None
        self.issuance_period: Optional[str] = None
        self.remark: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecurringPaymentForCreateBuilder":
        return RecurringPaymentForCreateBuilder()


class RecurringPaymentForCreateBuilder(object):
    def __init__(self) -> None:
        self._recurring_payment_for_create = RecurringPaymentForCreate()

    def unique_id(self, unique_id: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.unique_id = unique_id
        return self

    def user_id(self, user_id: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.user_id = user_id
        return self

    def item_id(self, item_id: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.item_id = item_id
        return self

    def each_amount(self, each_amount: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.each_amount = each_amount
        return self

    def start_date(self, start_date: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.start_date = start_date
        return self

    def end_date(self, end_date: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.end_date = end_date
        return self

    def currency_id(self, currency_id: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.currency_id = currency_id
        return self

    def issuance_type(self, issuance_type: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.issuance_type = issuance_type
        return self

    def issuance_period(self, issuance_period: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.issuance_period = issuance_period
        return self

    def remark(self, remark: str) -> "RecurringPaymentForCreateBuilder":
        self._recurring_payment_for_create.remark = remark
        return self

    def build(self) -> "RecurringPaymentForCreate":
        return self._recurring_payment_for_create
