# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ApplicationTalentLanguageInfo(object):
    _types = {
        "id": str,
        "language": int,
        "proficiency": int,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.language: Optional[int] = None
        self.proficiency: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationTalentLanguageInfoBuilder":
        return ApplicationTalentLanguageInfoBuilder()


class ApplicationTalentLanguageInfoBuilder(object):
    def __init__(self, application_talent_language_info: ApplicationTalentLanguageInfo = ApplicationTalentLanguageInfo({})) -> None:
        self._application_talent_language_info: ApplicationTalentLanguageInfo = application_talent_language_info
    
    def id(self, id: str) -> "ApplicationTalentLanguageInfoBuilder":
        self._application_talent_language_info.id = id
        return self
    
    def language(self, language: int) -> "ApplicationTalentLanguageInfoBuilder":
        self._application_talent_language_info.language = language
        return self
    
    def proficiency(self, proficiency: int) -> "ApplicationTalentLanguageInfoBuilder":
        self._application_talent_language_info.proficiency = proficiency
        return self
    
    def build(self) -> "ApplicationTalentLanguageInfo":
        return self._application_talent_language_info