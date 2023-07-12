# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class QuoteContainer(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QuoteContainerBuilder":
        return QuoteContainerBuilder()


class QuoteContainerBuilder(object):
    def __init__(self, quote_container: QuoteContainer = QuoteContainer({})) -> None:
        self._quote_container: QuoteContainer = quote_container
    
    def build(self) -> "QuoteContainer":
        return self._quote_container