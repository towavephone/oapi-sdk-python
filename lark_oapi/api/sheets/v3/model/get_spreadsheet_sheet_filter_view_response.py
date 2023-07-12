# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_spreadsheet_sheet_filter_view_response_body import GetSpreadsheetSheetFilterViewResponseBody


class GetSpreadsheetSheetFilterViewResponse(BaseResponse):
    _types = {
        "data": GetSpreadsheetSheetFilterViewResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetSpreadsheetSheetFilterViewResponseBody] = None
        init(self, d, self._types)
