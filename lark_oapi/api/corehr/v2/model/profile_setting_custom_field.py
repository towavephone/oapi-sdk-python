# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ProfileSettingCustomField(object):
    _types = {
        "field_name": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.field_name: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingCustomFieldBuilder":
        return ProfileSettingCustomFieldBuilder()


class ProfileSettingCustomFieldBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_custom_field = ProfileSettingCustomField()

    def field_name(self, field_name: str) -> "ProfileSettingCustomFieldBuilder":
        self._profile_setting_custom_field.field_name = field_name
        return self

    def value(self, value: str) -> "ProfileSettingCustomFieldBuilder":
        self._profile_setting_custom_field.value = value
        return self

    def build(self) -> "ProfileSettingCustomField":
        return self._profile_setting_custom_field
