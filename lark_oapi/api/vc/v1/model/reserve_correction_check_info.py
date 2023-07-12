# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ReserveCorrectionCheckInfo(object):
    _types = {
        "invalid_host_id_list": List[str],
    }

    def __init__(self, d):
        self.invalid_host_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveCorrectionCheckInfoBuilder":
        return ReserveCorrectionCheckInfoBuilder()


class ReserveCorrectionCheckInfoBuilder(object):
    def __init__(self, reserve_correction_check_info: ReserveCorrectionCheckInfo = ReserveCorrectionCheckInfo({})) -> None:
        self._reserve_correction_check_info: ReserveCorrectionCheckInfo = reserve_correction_check_info
    
    def invalid_host_id_list(self, invalid_host_id_list: List[str]) -> "ReserveCorrectionCheckInfoBuilder":
        self._reserve_correction_check_info.invalid_host_id_list = invalid_host_id_list
        return self
    
    def build(self) -> "ReserveCorrectionCheckInfo":
        return self._reserve_correction_check_info