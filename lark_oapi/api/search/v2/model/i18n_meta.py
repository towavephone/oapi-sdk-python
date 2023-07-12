# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class I18nMeta(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
        "ja_jp": str,
    }

    def __init__(self, d):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        self.ja_jp: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "I18nMetaBuilder":
        return I18nMetaBuilder()


class I18nMetaBuilder(object):
    def __init__(self, i18n_meta: I18nMeta = I18nMeta({})) -> None:
        self._i18n_meta: I18nMeta = i18n_meta
    
    def zh_cn(self, zh_cn: str) -> "I18nMetaBuilder":
        self._i18n_meta.zh_cn = zh_cn
        return self
    
    def en_us(self, en_us: str) -> "I18nMetaBuilder":
        self._i18n_meta.en_us = en_us
        return self
    
    def ja_jp(self, ja_jp: str) -> "I18nMetaBuilder":
        self._i18n_meta.ja_jp = ja_jp
        return self
    
    def build(self) -> "I18nMeta":
        return self._i18n_meta