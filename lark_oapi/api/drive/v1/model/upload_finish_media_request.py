# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .upload_finish_media_request_body import UploadFinishMediaRequestBody


class UploadFinishMediaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[UploadFinishMediaRequestBody] = None

    @staticmethod
    def builder() -> "UploadFinishMediaRequestBuilder":
        return UploadFinishMediaRequestBuilder()


class UploadFinishMediaRequestBuilder(object):

    def __init__(self, upload_finish_media_request: UploadFinishMediaRequest = UploadFinishMediaRequest()) -> None:
        upload_finish_media_request.http_method = HttpMethod.POST
        upload_finish_media_request.uri = "/open-apis/drive/v1/medias/upload_finish"
        upload_finish_media_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._upload_finish_media_request: UploadFinishMediaRequest = upload_finish_media_request
    
    def request_body(self, request_body: UploadFinishMediaRequestBody) -> "UploadFinishMediaRequestBuilder":
        self._upload_finish_media_request.request_body = request_body
        self._upload_finish_media_request.body = request_body
        return self

    def build(self) -> UploadFinishMediaRequest:
        return self._upload_finish_media_request
