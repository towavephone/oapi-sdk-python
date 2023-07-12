# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .replace_spreadsheet_sheet_response_body import ReplaceSpreadsheetSheetResponseBody


class ReplaceSpreadsheetSheetResponse(BaseResponse):
    _types = {
        "data": ReplaceSpreadsheetSheetResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ReplaceSpreadsheetSheetResponseBody] = None
        init(self, d, self._types)
