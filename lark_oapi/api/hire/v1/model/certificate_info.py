# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CertificateInfo(object):
    _types = {
        "desc": str,
        "name": str,
    }

    def __init__(self, d):
        self.desc: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CertificateInfoBuilder":
        return CertificateInfoBuilder()


class CertificateInfoBuilder(object):
    def __init__(self, certificate_info: CertificateInfo = CertificateInfo({})) -> None:
        self._certificate_info: CertificateInfo = certificate_info
    
    def desc(self, desc: str) -> "CertificateInfoBuilder":
        self._certificate_info.desc = desc
        return self
    
    def name(self, name: str) -> "CertificateInfoBuilder":
        self._certificate_info.name = name
        return self
    
    def build(self) -> "CertificateInfo":
        return self._certificate_info