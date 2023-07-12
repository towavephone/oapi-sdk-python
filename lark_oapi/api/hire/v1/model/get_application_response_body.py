# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .application import Application


class GetApplicationResponseBody(object):
    _types = {
        "application": Application,
    }

    def __init__(self, d):
        self.application: Optional[Application] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetApplicationResponseBodyBuilder":
        return GetApplicationResponseBodyBuilder()


class GetApplicationResponseBodyBuilder(object):
    def __init__(self, get_application_response_body: GetApplicationResponseBody = GetApplicationResponseBody({})) -> None:
        self._get_application_response_body: GetApplicationResponseBody = get_application_response_body
    
    def application(self, application: Application) -> "GetApplicationResponseBodyBuilder":
        self._get_application_response_body.application = application
        return self
    
    def build(self) -> "GetApplicationResponseBody":
        return self._get_application_response_body