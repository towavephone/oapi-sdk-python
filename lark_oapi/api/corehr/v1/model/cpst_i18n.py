# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CpstI18n(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CpstI18nBuilder":
        return CpstI18nBuilder()


class CpstI18nBuilder(object):
    def __init__(self, cpst_i18n: CpstI18n = CpstI18n({})) -> None:
        self._cpst_i18n: CpstI18n = cpst_i18n
    
    def zh_cn(self, zh_cn: str) -> "CpstI18nBuilder":
        self._cpst_i18n.zh_cn = zh_cn
        return self
    
    def en_us(self, en_us: str) -> "CpstI18nBuilder":
        self._cpst_i18n.en_us = en_us
        return self
    
    def build(self) -> "CpstI18n":
        return self._cpst_i18n