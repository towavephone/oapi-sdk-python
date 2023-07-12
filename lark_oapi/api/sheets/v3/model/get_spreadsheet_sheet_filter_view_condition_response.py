# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_spreadsheet_sheet_filter_view_condition_response_body import GetSpreadsheetSheetFilterViewConditionResponseBody


class GetSpreadsheetSheetFilterViewConditionResponse(BaseResponse):
    _types = {
        "data": GetSpreadsheetSheetFilterViewConditionResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetSpreadsheetSheetFilterViewConditionResponseBody] = None
        init(self, d, self._types)
