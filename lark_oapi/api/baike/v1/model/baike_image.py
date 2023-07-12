# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class BaikeImage(object):
    _types = {
        "token": str,
    }

    def __init__(self, d):
        self.token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BaikeImageBuilder":
        return BaikeImageBuilder()


class BaikeImageBuilder(object):
    def __init__(self, baike_image: BaikeImage = BaikeImage({})) -> None:
        self._baike_image: BaikeImage = baike_image
    
    def token(self, token: str) -> "BaikeImageBuilder":
        self._baike_image.token = token
        return self
    
    def build(self) -> "BaikeImage":
        return self._baike_image