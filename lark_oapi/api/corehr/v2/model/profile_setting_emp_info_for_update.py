# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .profile_setting_emp_basic_info_for_update import ProfileSettingEmpBasicInfoForUpdate
from .profile_setting_probation_info import ProfileSettingProbationInfo
from .profile_setting_custom_group import ProfileSettingCustomGroup


class ProfileSettingEmpInfoForUpdate(object):
    _types = {
        "basic_info": ProfileSettingEmpBasicInfoForUpdate,
        "probation_info": ProfileSettingProbationInfo,
        "custom_groups": List[ProfileSettingCustomGroup],
    }

    def __init__(self, d=None):
        self.basic_info: Optional[ProfileSettingEmpBasicInfoForUpdate] = None
        self.probation_info: Optional[ProfileSettingProbationInfo] = None
        self.custom_groups: Optional[List[ProfileSettingCustomGroup]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingEmpInfoForUpdateBuilder":
        return ProfileSettingEmpInfoForUpdateBuilder()


class ProfileSettingEmpInfoForUpdateBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_emp_info_for_update = ProfileSettingEmpInfoForUpdate()

    def basic_info(self, basic_info: ProfileSettingEmpBasicInfoForUpdate) -> "ProfileSettingEmpInfoForUpdateBuilder":
        self._profile_setting_emp_info_for_update.basic_info = basic_info
        return self

    def probation_info(self, probation_info: ProfileSettingProbationInfo) -> "ProfileSettingEmpInfoForUpdateBuilder":
        self._profile_setting_emp_info_for_update.probation_info = probation_info
        return self

    def custom_groups(self, custom_groups: List[ProfileSettingCustomGroup]) -> "ProfileSettingEmpInfoForUpdateBuilder":
        self._profile_setting_emp_info_for_update.custom_groups = custom_groups
        return self

    def build(self) -> "ProfileSettingEmpInfoForUpdate":
        return self._profile_setting_emp_info_for_update
