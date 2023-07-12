# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ImageFieldSetting(object):
    _types = {
        "image_type": int,
        "display_style": int,
    }

    def __init__(self, d):
        self.image_type: Optional[int] = None
        self.display_style: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImageFieldSettingBuilder":
        return ImageFieldSettingBuilder()


class ImageFieldSettingBuilder(object):
    def __init__(self, image_field_setting: ImageFieldSetting = ImageFieldSetting({})) -> None:
        self._image_field_setting: ImageFieldSetting = image_field_setting
    
    def image_type(self, image_type: int) -> "ImageFieldSettingBuilder":
        self._image_field_setting.image_type = image_type
        return self
    
    def display_style(self, display_style: int) -> "ImageFieldSettingBuilder":
        self._image_field_setting.display_style = display_style
        return self
    
    def build(self) -> "ImageFieldSetting":
        return self._image_field_setting