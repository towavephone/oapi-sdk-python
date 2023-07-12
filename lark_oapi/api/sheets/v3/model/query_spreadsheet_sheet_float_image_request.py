# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class QuerySpreadsheetSheetFloatImageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None

    @staticmethod
    def builder() -> "QuerySpreadsheetSheetFloatImageRequestBuilder":
        return QuerySpreadsheetSheetFloatImageRequestBuilder()


class QuerySpreadsheetSheetFloatImageRequestBuilder(object):

    def __init__(self, query_spreadsheet_sheet_float_image_request: QuerySpreadsheetSheetFloatImageRequest = QuerySpreadsheetSheetFloatImageRequest()) -> None:
        query_spreadsheet_sheet_float_image_request.http_method = HttpMethod.GET
        query_spreadsheet_sheet_float_image_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images/query"
        query_spreadsheet_sheet_float_image_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._query_spreadsheet_sheet_float_image_request: QuerySpreadsheetSheetFloatImageRequest = query_spreadsheet_sheet_float_image_request
    
    def spreadsheet_token(self, spreadsheet_token: str) -> "QuerySpreadsheetSheetFloatImageRequestBuilder":
        self._query_spreadsheet_sheet_float_image_request.spreadsheet_token = spreadsheet_token
        self._query_spreadsheet_sheet_float_image_request.paths["spreadsheet_token"] = spreadsheet_token
        return self
    
    def sheet_id(self, sheet_id: str) -> "QuerySpreadsheetSheetFloatImageRequestBuilder":
        self._query_spreadsheet_sheet_float_image_request.sheet_id = sheet_id
        self._query_spreadsheet_sheet_float_image_request.paths["sheet_id"] = sheet_id
        return self
    

    def build(self) -> QuerySpreadsheetSheetFloatImageRequest:
        return self._query_spreadsheet_sheet_float_image_request
