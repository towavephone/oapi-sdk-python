# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetTopUserReportRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.limit: Optional[int] = None
        self.order_by: Optional[int] = None
        self.unit: Optional[int] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "GetTopUserReportRequestBuilder":
        return GetTopUserReportRequestBuilder()


class GetTopUserReportRequestBuilder(object):

    def __init__(self) -> None:
        get_top_user_report_request = GetTopUserReportRequest()
        get_top_user_report_request.http_method = HttpMethod.GET
        get_top_user_report_request.uri = "/open-apis/vc/v1/reports/get_top_user"
        get_top_user_report_request.token_types = {AccessTokenType.TENANT}
        self._get_top_user_report_request: GetTopUserReportRequest = get_top_user_report_request

    def start_time(self, start_time: int) -> "GetTopUserReportRequestBuilder":
        self._get_top_user_report_request.start_time = start_time
        self._get_top_user_report_request.add_query("start_time", start_time)
        return self

    def end_time(self, end_time: int) -> "GetTopUserReportRequestBuilder":
        self._get_top_user_report_request.end_time = end_time
        self._get_top_user_report_request.add_query("end_time", end_time)
        return self

    def limit(self, limit: int) -> "GetTopUserReportRequestBuilder":
        self._get_top_user_report_request.limit = limit
        self._get_top_user_report_request.add_query("limit", limit)
        return self

    def order_by(self, order_by: int) -> "GetTopUserReportRequestBuilder":
        self._get_top_user_report_request.order_by = order_by
        self._get_top_user_report_request.add_query("order_by", order_by)
        return self

    def unit(self, unit: int) -> "GetTopUserReportRequestBuilder":
        self._get_top_user_report_request.unit = unit
        self._get_top_user_report_request.add_query("unit", unit)
        return self

    def user_id_type(self, user_id_type: str) -> "GetTopUserReportRequestBuilder":
        self._get_top_user_report_request.user_id_type = user_id_type
        self._get_top_user_report_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> GetTopUserReportRequest:
        return self._get_top_user_report_request
