# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CreateExchangeBindingResponseBody(object):
    _types = {
        "admin_account": str,
        "exchange_account": str,
        "user_id": str,
        "status": str,
        "exchange_binding_id": str,
    }

    def __init__(self, d):
        self.admin_account: Optional[str] = None
        self.exchange_account: Optional[str] = None
        self.user_id: Optional[str] = None
        self.status: Optional[str] = None
        self.exchange_binding_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateExchangeBindingResponseBodyBuilder":
        return CreateExchangeBindingResponseBodyBuilder()


class CreateExchangeBindingResponseBodyBuilder(object):
    def __init__(self, create_exchange_binding_response_body: CreateExchangeBindingResponseBody = CreateExchangeBindingResponseBody({})) -> None:
        self._create_exchange_binding_response_body: CreateExchangeBindingResponseBody = create_exchange_binding_response_body
    
    def admin_account(self, admin_account: str) -> "CreateExchangeBindingResponseBodyBuilder":
        self._create_exchange_binding_response_body.admin_account = admin_account
        return self
    
    def exchange_account(self, exchange_account: str) -> "CreateExchangeBindingResponseBodyBuilder":
        self._create_exchange_binding_response_body.exchange_account = exchange_account
        return self
    
    def user_id(self, user_id: str) -> "CreateExchangeBindingResponseBodyBuilder":
        self._create_exchange_binding_response_body.user_id = user_id
        return self
    
    def status(self, status: str) -> "CreateExchangeBindingResponseBodyBuilder":
        self._create_exchange_binding_response_body.status = status
        return self
    
    def exchange_binding_id(self, exchange_binding_id: str) -> "CreateExchangeBindingResponseBodyBuilder":
        self._create_exchange_binding_response_body.exchange_binding_id = exchange_binding_id
        return self
    
    def build(self) -> "CreateExchangeBindingResponseBody":
        return self._create_exchange_binding_response_body