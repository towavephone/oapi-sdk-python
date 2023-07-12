# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Image(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImageBuilder":
        return ImageBuilder()


class ImageBuilder(object):
    def __init__(self, image: Image = Image({})) -> None:
        self._image: Image = image
    
    def build(self) -> "Image":
        return self._image