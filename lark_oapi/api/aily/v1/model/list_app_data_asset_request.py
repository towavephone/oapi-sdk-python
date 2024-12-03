# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListAppDataAssetRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.keyword: Optional[str] = None
        self.data_asset_ids: Optional[List[str]] = None
        self.data_asset_tag_ids: Optional[List[str]] = None
        self.with_data_asset_item: Optional[bool] = None
        self.with_connect_status: Optional[bool] = None
        self.app_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListAppDataAssetRequestBuilder":
        return ListAppDataAssetRequestBuilder()


class ListAppDataAssetRequestBuilder(object):

    def __init__(self) -> None:
        list_app_data_asset_request = ListAppDataAssetRequest()
        list_app_data_asset_request.http_method = HttpMethod.GET
        list_app_data_asset_request.uri = "/open-apis/aily/v1/apps/:app_id/data_assets"
        list_app_data_asset_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_app_data_asset_request: ListAppDataAssetRequest = list_app_data_asset_request

    def page_size(self, page_size: int) -> "ListAppDataAssetRequestBuilder":
        self._list_app_data_asset_request.page_size = page_size
        self._list_app_data_asset_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListAppDataAssetRequestBuilder":
        self._list_app_data_asset_request.page_token = page_token
        self._list_app_data_asset_request.add_query("page_token", page_token)
        return self

    def keyword(self, keyword: str) -> "ListAppDataAssetRequestBuilder":
        self._list_app_data_asset_request.keyword = keyword
        self._list_app_data_asset_request.add_query("keyword", keyword)
        return self

    def data_asset_ids(self, data_asset_ids: List[str]) -> "ListAppDataAssetRequestBuilder":
        self._list_app_data_asset_request.data_asset_ids = data_asset_ids
        self._list_app_data_asset_request.add_query("data_asset_ids", data_asset_ids)
        return self

    def data_asset_tag_ids(self, data_asset_tag_ids: List[str]) -> "ListAppDataAssetRequestBuilder":
        self._list_app_data_asset_request.data_asset_tag_ids = data_asset_tag_ids
        self._list_app_data_asset_request.add_query("data_asset_tag_ids", data_asset_tag_ids)
        return self

    def with_data_asset_item(self, with_data_asset_item: bool) -> "ListAppDataAssetRequestBuilder":
        self._list_app_data_asset_request.with_data_asset_item = with_data_asset_item
        self._list_app_data_asset_request.add_query("with_data_asset_item", with_data_asset_item)
        return self

    def with_connect_status(self, with_connect_status: bool) -> "ListAppDataAssetRequestBuilder":
        self._list_app_data_asset_request.with_connect_status = with_connect_status
        self._list_app_data_asset_request.add_query("with_connect_status", with_connect_status)
        return self

    def app_id(self, app_id: str) -> "ListAppDataAssetRequestBuilder":
        self._list_app_data_asset_request.app_id = app_id
        self._list_app_data_asset_request.paths["app_id"] = str(app_id)
        return self

    def build(self) -> ListAppDataAssetRequest:
        return self._list_app_data_asset_request
