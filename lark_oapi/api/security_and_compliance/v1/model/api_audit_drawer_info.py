# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ApiAuditDrawerInfo(object):
    _types = {
        "info_key": str,
        "info_val": str,
        "key_i18n_key": str,
        "val_type": str,
        "val_i18n_key": str,
    }

    def __init__(self, d=None):
        self.info_key: Optional[str] = None
        self.info_val: Optional[str] = None
        self.key_i18n_key: Optional[str] = None
        self.val_type: Optional[str] = None
        self.val_i18n_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApiAuditDrawerInfoBuilder":
        return ApiAuditDrawerInfoBuilder()


class ApiAuditDrawerInfoBuilder(object):
    def __init__(self) -> None:
        self._api_audit_drawer_info = ApiAuditDrawerInfo()

    def info_key(self, info_key: str) -> "ApiAuditDrawerInfoBuilder":
        self._api_audit_drawer_info.info_key = info_key
        return self

    def info_val(self, info_val: str) -> "ApiAuditDrawerInfoBuilder":
        self._api_audit_drawer_info.info_val = info_val
        return self

    def key_i18n_key(self, key_i18n_key: str) -> "ApiAuditDrawerInfoBuilder":
        self._api_audit_drawer_info.key_i18n_key = key_i18n_key
        return self

    def val_type(self, val_type: str) -> "ApiAuditDrawerInfoBuilder":
        self._api_audit_drawer_info.val_type = val_type
        return self

    def val_i18n_key(self, val_i18n_key: str) -> "ApiAuditDrawerInfoBuilder":
        self._api_audit_drawer_info.val_i18n_key = val_i18n_key
        return self

    def build(self) -> "ApiAuditDrawerInfo":
        return self._api_audit_drawer_info
