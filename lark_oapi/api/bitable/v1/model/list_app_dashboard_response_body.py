# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .app_dashboard import AppDashboard


class ListAppDashboardResponseBody(object):
    _types = {
        "dashboards": List[AppDashboard],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d):
        self.dashboards: Optional[List[AppDashboard]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAppDashboardResponseBodyBuilder":
        return ListAppDashboardResponseBodyBuilder()


class ListAppDashboardResponseBodyBuilder(object):
    def __init__(self, list_app_dashboard_response_body: ListAppDashboardResponseBody = ListAppDashboardResponseBody({})) -> None:
        self._list_app_dashboard_response_body: ListAppDashboardResponseBody = list_app_dashboard_response_body
    
    def dashboards(self, dashboards: List[AppDashboard]) -> "ListAppDashboardResponseBodyBuilder":
        self._list_app_dashboard_response_body.dashboards = dashboards
        return self
    
    def page_token(self, page_token: str) -> "ListAppDashboardResponseBodyBuilder":
        self._list_app_dashboard_response_body.page_token = page_token
        return self
    
    def has_more(self, has_more: bool) -> "ListAppDashboardResponseBodyBuilder":
        self._list_app_dashboard_response_body.has_more = has_more
        return self
    
    def build(self) -> "ListAppDashboardResponseBody":
        return self._list_app_dashboard_response_body