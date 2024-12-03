# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .edit_enum_option_common_data_meta_data_request_body import EditEnumOptionCommonDataMetaDataRequestBody


class EditEnumOptionCommonDataMetaDataRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[EditEnumOptionCommonDataMetaDataRequestBody] = None

    @staticmethod
    def builder() -> "EditEnumOptionCommonDataMetaDataRequestBuilder":
        return EditEnumOptionCommonDataMetaDataRequestBuilder()


class EditEnumOptionCommonDataMetaDataRequestBuilder(object):

    def __init__(self) -> None:
        edit_enum_option_common_data_meta_data_request = EditEnumOptionCommonDataMetaDataRequest()
        edit_enum_option_common_data_meta_data_request.http_method = HttpMethod.POST
        edit_enum_option_common_data_meta_data_request.uri = "/open-apis/corehr/v1/common_data/meta_data/edit_enum_option"
        edit_enum_option_common_data_meta_data_request.token_types = {AccessTokenType.TENANT}
        self._edit_enum_option_common_data_meta_data_request: EditEnumOptionCommonDataMetaDataRequest = edit_enum_option_common_data_meta_data_request

    def client_token(self, client_token: str) -> "EditEnumOptionCommonDataMetaDataRequestBuilder":
        self._edit_enum_option_common_data_meta_data_request.client_token = client_token
        self._edit_enum_option_common_data_meta_data_request.add_query("client_token", client_token)
        return self

    def request_body(self,
                     request_body: EditEnumOptionCommonDataMetaDataRequestBody) -> "EditEnumOptionCommonDataMetaDataRequestBuilder":
        self._edit_enum_option_common_data_meta_data_request.request_body = request_body
        self._edit_enum_option_common_data_meta_data_request.body = request_body
        return self

    def build(self) -> EditEnumOptionCommonDataMetaDataRequest:
        return self._edit_enum_option_common_data_meta_data_request
