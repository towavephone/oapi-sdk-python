# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .profile_setting_custom_group import ProfileSettingCustomGroup
from .profile_setting_education import ProfileSettingEducation
from .profile_setting_work_experience import ProfileSettingWorkExperience


class ProfileSettingCareer(object):
    _types = {
        "educations": List[ProfileSettingEducation],
        "work_experiences": List[ProfileSettingWorkExperience],
        "custom_groups": List[ProfileSettingCustomGroup],
    }

    def __init__(self, d=None):
        self.educations: Optional[List[ProfileSettingEducation]] = None
        self.work_experiences: Optional[List[ProfileSettingWorkExperience]] = None
        self.custom_groups: Optional[List[ProfileSettingCustomGroup]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingCareerBuilder":
        return ProfileSettingCareerBuilder()


class ProfileSettingCareerBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_career = ProfileSettingCareer()

    def educations(self, educations: List[ProfileSettingEducation]) -> "ProfileSettingCareerBuilder":
        self._profile_setting_career.educations = educations
        return self

    def work_experiences(self, work_experiences: List[ProfileSettingWorkExperience]) -> "ProfileSettingCareerBuilder":
        self._profile_setting_career.work_experiences = work_experiences
        return self

    def custom_groups(self, custom_groups: List[ProfileSettingCustomGroup]) -> "ProfileSettingCareerBuilder":
        self._profile_setting_career.custom_groups = custom_groups
        return self

    def build(self) -> "ProfileSettingCareer":
        return self._profile_setting_career
