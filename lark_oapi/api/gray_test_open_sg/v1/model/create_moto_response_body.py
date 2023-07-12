# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .moto import Moto


class CreateMotoResponseBody(object):
    _types = {
        "moto": Moto,
    }

    def __init__(self, d):
        self.moto: Optional[Moto] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateMotoResponseBodyBuilder":
        return CreateMotoResponseBodyBuilder()


class CreateMotoResponseBodyBuilder(object):
    def __init__(self, create_moto_response_body: CreateMotoResponseBody = CreateMotoResponseBody({})) -> None:
        self._create_moto_response_body: CreateMotoResponseBody = create_moto_response_body
    
    def moto(self, moto: Moto) -> "CreateMotoResponseBodyBuilder":
        self._create_moto_response_body.moto = moto
        return self
    
    def build(self) -> "CreateMotoResponseBody":
        return self._create_moto_response_body