# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v1.resource import *


class AdminService(object):
    def __init__(self, config: Config) -> None:
        self.v1: V1 = V1(config)


class V1(object):
    def __init__(self, config: Config) -> None:
        self.admin_dept_stat: Optional[AdminDeptStat] = AdminDeptStat(config)
        self.admin_user_stat: Optional[AdminUserStat] = AdminUserStat(config)
        self.badge: Optional[Badge] = Badge(config)
        self.badge_grant: Optional[BadgeGrant] = BadgeGrant(config)
        self.badge_image: Optional[BadgeImage] = BadgeImage(config)
        self.password: Optional[Password] = Password(config)