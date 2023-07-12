# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_document_response_body import CreateDocumentResponseBody


class CreateDocumentResponse(BaseResponse):
    _types = {
        "data": CreateDocumentResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateDocumentResponseBody] = None
        init(self, d, self._types)
