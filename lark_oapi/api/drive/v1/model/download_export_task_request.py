# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DownloadExportTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_token: Optional[str] = None

    @staticmethod
    def builder() -> "DownloadExportTaskRequestBuilder":
        return DownloadExportTaskRequestBuilder()


class DownloadExportTaskRequestBuilder(object):

    def __init__(self, download_export_task_request: DownloadExportTaskRequest = DownloadExportTaskRequest()) -> None:
        download_export_task_request.http_method = HttpMethod.GET
        download_export_task_request.uri = "/open-apis/drive/v1/export_tasks/file/:file_token/download"
        download_export_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._download_export_task_request: DownloadExportTaskRequest = download_export_task_request
    
    def file_token(self, file_token: str) -> "DownloadExportTaskRequestBuilder":
        self._download_export_task_request.file_token = file_token
        self._download_export_task_request.paths["file_token"] = file_token
        return self
    

    def build(self) -> DownloadExportTaskRequest:
        return self._download_export_task_request
