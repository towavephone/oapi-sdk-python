# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v1.resource import *


class AcsService(object):
    def __init__(self, config: Config) -> None:
        self.v1: V1 = V1(config)


class V1(object):
    def __init__(self, config: Config) -> None:
        self.access_record: Optional[AccessRecord] = AccessRecord(config)
        self.access_record_access_photo: Optional[AccessRecordAccessPhoto] = AccessRecordAccessPhoto(config)
        self.device: Optional[Device] = Device(config)
        self.user: Optional[User] = User(config)
        self.user_face: Optional[UserFace] = UserFace(config)