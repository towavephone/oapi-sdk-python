# Code generated by Lark OpenAPI.

import io
from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from ..model.active_location_request import ActiveLocationRequest
from ..model.active_location_response import ActiveLocationResponse
from ..model.batch_get_location_request import BatchGetLocationRequest
from ..model.batch_get_location_response import BatchGetLocationResponse
from ..model.patch_location_request import PatchLocationRequest
from ..model.patch_location_response import PatchLocationResponse


class Location(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def active(self, request: ActiveLocationRequest, option: Optional[RequestOption] = None) -> ActiveLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ActiveLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), ActiveLocationResponse)
        response.raw = resp

        return response

    async def aactive(self, request: ActiveLocationRequest,
                      option: Optional[RequestOption] = None) -> ActiveLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ActiveLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), ActiveLocationResponse)
        response.raw = resp

        return response

    def batch_get(self, request: BatchGetLocationRequest,
                  option: Optional[RequestOption] = None) -> BatchGetLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchGetLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchGetLocationResponse)
        response.raw = resp

        return response

    async def abatch_get(self, request: BatchGetLocationRequest,
                         option: Optional[RequestOption] = None) -> BatchGetLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: BatchGetLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchGetLocationResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchLocationRequest, option: Optional[RequestOption] = None) -> PatchLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchLocationResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchLocationRequest,
                     option: Optional[RequestOption] = None) -> PatchLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchLocationResponse)
        response.raw = resp

        return response
