# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .contract import Contract


class CreateContractResponseBody(object):
    _types = {
        "contract": Contract,
    }

    def __init__(self, d):
        self.contract: Optional[Contract] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateContractResponseBodyBuilder":
        return CreateContractResponseBodyBuilder()


class CreateContractResponseBodyBuilder(object):
    def __init__(self, create_contract_response_body: CreateContractResponseBody = CreateContractResponseBody({})) -> None:
        self._create_contract_response_body: CreateContractResponseBody = create_contract_response_body
    
    def contract(self, contract: Contract) -> "CreateContractResponseBodyBuilder":
        self._create_contract_response_body.contract = contract
        return self
    
    def build(self) -> "CreateContractResponseBody":
        return self._create_contract_response_body