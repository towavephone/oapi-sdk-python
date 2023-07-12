# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class AppliTalentCertificateInfo(object):
    _types = {
        "id": str,
        "name": str,
        "desc": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.desc: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppliTalentCertificateInfoBuilder":
        return AppliTalentCertificateInfoBuilder()


class AppliTalentCertificateInfoBuilder(object):
    def __init__(self, appli_talent_certificate_info: AppliTalentCertificateInfo = AppliTalentCertificateInfo({})) -> None:
        self._appli_talent_certificate_info: AppliTalentCertificateInfo = appli_talent_certificate_info
    
    def id(self, id: str) -> "AppliTalentCertificateInfoBuilder":
        self._appli_talent_certificate_info.id = id
        return self
    
    def name(self, name: str) -> "AppliTalentCertificateInfoBuilder":
        self._appli_talent_certificate_info.name = name
        return self
    
    def desc(self, desc: str) -> "AppliTalentCertificateInfoBuilder":
        self._appli_talent_certificate_info.desc = desc
        return self
    
    def build(self) -> "AppliTalentCertificateInfo":
        return self._appli_talent_certificate_info