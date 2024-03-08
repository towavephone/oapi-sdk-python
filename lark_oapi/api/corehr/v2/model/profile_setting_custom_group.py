# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .profile_setting_custom_group_item import ProfileSettingCustomGroupItem


class ProfileSettingCustomGroup(object):
    _types = {
        "group_name": str,
        "items": List[ProfileSettingCustomGroupItem],
    }

    def __init__(self, d=None):
        self.group_name: Optional[str] = None
        self.items: Optional[List[ProfileSettingCustomGroupItem]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingCustomGroupBuilder":
        return ProfileSettingCustomGroupBuilder()


class ProfileSettingCustomGroupBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_custom_group = ProfileSettingCustomGroup()

    def group_name(self, group_name: str) -> "ProfileSettingCustomGroupBuilder":
        self._profile_setting_custom_group.group_name = group_name
        return self

    def items(self, items: List[ProfileSettingCustomGroupItem]) -> "ProfileSettingCustomGroupBuilder":
        self._profile_setting_custom_group.items = items
        return self

    def build(self) -> "ProfileSettingCustomGroup":
        return self._profile_setting_custom_group
