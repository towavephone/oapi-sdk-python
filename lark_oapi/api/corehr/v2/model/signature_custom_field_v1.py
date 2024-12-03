# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SignatureCustomFieldV1(object):
    _types = {
        "key": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SignatureCustomFieldV1Builder":
        return SignatureCustomFieldV1Builder()


class SignatureCustomFieldV1Builder(object):
    def __init__(self) -> None:
        self._signature_custom_field_v1 = SignatureCustomFieldV1()

    def key(self, key: str) -> "SignatureCustomFieldV1Builder":
        self._signature_custom_field_v1.key = key
        return self

    def value(self, value: str) -> "SignatureCustomFieldV1Builder":
        self._signature_custom_field_v1.value = value
        return self

    def build(self) -> "SignatureCustomFieldV1":
        return self._signature_custom_field_v1
