# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListTalentFolderRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListTalentFolderRequestBuilder":
        return ListTalentFolderRequestBuilder()


class ListTalentFolderRequestBuilder(object):

    def __init__(self, list_talent_folder_request: ListTalentFolderRequest = ListTalentFolderRequest()) -> None:
        list_talent_folder_request.http_method = HttpMethod.GET
        list_talent_folder_request.uri = "/open-apis/hire/v1/talent_folders"
        list_talent_folder_request.token_types = {AccessTokenType.TENANT}
        self._list_talent_folder_request: ListTalentFolderRequest = list_talent_folder_request
    
    def page_token(self, page_token: str) -> "ListTalentFolderRequestBuilder":
        self._list_talent_folder_request.page_token = page_token
        self._list_talent_folder_request.queries["page_token"] = str(page_token)
        return self
    
    def page_size(self, page_size: int) -> "ListTalentFolderRequestBuilder":
        self._list_talent_folder_request.page_size = page_size
        self._list_talent_folder_request.queries["page_size"] = str(page_size)
        return self
    
    def user_id_type(self, user_id_type: str) -> "ListTalentFolderRequestBuilder":
        self._list_talent_folder_request.user_id_type = user_id_type
        self._list_talent_folder_request.queries["user_id_type"] = str(user_id_type)
        return self
    

    def build(self) -> ListTalentFolderRequest:
        return self._list_talent_folder_request
