# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ProfileSettingProbationInfo(object):
    _types = {
        "probation_start_date": str,
        "probation_expected_end_date": str,
        "actual_probation_end_date": str,
    }

    def __init__(self, d=None):
        self.probation_start_date: Optional[str] = None
        self.probation_expected_end_date: Optional[str] = None
        self.actual_probation_end_date: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingProbationInfoBuilder":
        return ProfileSettingProbationInfoBuilder()


class ProfileSettingProbationInfoBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_probation_info = ProfileSettingProbationInfo()

    def probation_start_date(self, probation_start_date: str) -> "ProfileSettingProbationInfoBuilder":
        self._profile_setting_probation_info.probation_start_date = probation_start_date
        return self

    def probation_expected_end_date(self, probation_expected_end_date: str) -> "ProfileSettingProbationInfoBuilder":
        self._profile_setting_probation_info.probation_expected_end_date = probation_expected_end_date
        return self

    def actual_probation_end_date(self, actual_probation_end_date: str) -> "ProfileSettingProbationInfoBuilder":
        self._profile_setting_probation_info.actual_probation_end_date = actual_probation_end_date
        return self

    def build(self) -> "ProfileSettingProbationInfo":
        return self._profile_setting_probation_info
