# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class InternalAppAccessTokenRequestBody(object):
    _types = {
        "app_id": str,
        "app_secret": str,
    }

    def __init__(self, d):
        self.app_id: Optional[str] = None
        self.app_secret: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InternalAppAccessTokenRequestBodyBuilder":
        return InternalAppAccessTokenRequestBodyBuilder()


class InternalAppAccessTokenRequestBodyBuilder(object):
    def __init__(self, internal_app_access_token_request_body: InternalAppAccessTokenRequestBody = InternalAppAccessTokenRequestBody({})) -> None:
        self._internal_app_access_token_request_body: InternalAppAccessTokenRequestBody = internal_app_access_token_request_body
    
    def app_id(self, app_id: str) -> "InternalAppAccessTokenRequestBodyBuilder":
        self._internal_app_access_token_request_body.app_id = app_id
        return self
    
    def app_secret(self, app_secret: str) -> "InternalAppAccessTokenRequestBodyBuilder":
        self._internal_app_access_token_request_body.app_secret = app_secret
        return self
    
    def build(self) -> "InternalAppAccessTokenRequestBody":
        return self._internal_app_access_token_request_body