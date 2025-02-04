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
from ..model.cancel_aily_session_run_request import CancelAilySessionRunRequest
from ..model.cancel_aily_session_run_response import CancelAilySessionRunResponse
from ..model.create_aily_session_run_request import CreateAilySessionRunRequest
from ..model.create_aily_session_run_response import CreateAilySessionRunResponse
from ..model.get_aily_session_run_request import GetAilySessionRunRequest
from ..model.get_aily_session_run_response import GetAilySessionRunResponse
from ..model.list_aily_session_run_request import ListAilySessionRunRequest
from ..model.list_aily_session_run_response import ListAilySessionRunResponse


class AilySessionRun(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def cancel(self, request: CancelAilySessionRunRequest,
               option: Optional[RequestOption] = None) -> CancelAilySessionRunResponse:
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
        response: CancelAilySessionRunResponse = JSON.unmarshal(str(resp.content, UTF_8), CancelAilySessionRunResponse)
        response.raw = resp

        return response

    async def acancel(self, request: CancelAilySessionRunRequest,
                      option: Optional[RequestOption] = None) -> CancelAilySessionRunResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CancelAilySessionRunResponse = JSON.unmarshal(str(resp.content, UTF_8), CancelAilySessionRunResponse)
        response.raw = resp

        return response

    def create(self, request: CreateAilySessionRunRequest,
               option: Optional[RequestOption] = None) -> CreateAilySessionRunResponse:
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
        response: CreateAilySessionRunResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAilySessionRunResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateAilySessionRunRequest,
                      option: Optional[RequestOption] = None) -> CreateAilySessionRunResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateAilySessionRunResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAilySessionRunResponse)
        response.raw = resp

        return response

    def get(self, request: GetAilySessionRunRequest,
            option: Optional[RequestOption] = None) -> GetAilySessionRunResponse:
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
        response: GetAilySessionRunResponse = JSON.unmarshal(str(resp.content, UTF_8), GetAilySessionRunResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetAilySessionRunRequest,
                   option: Optional[RequestOption] = None) -> GetAilySessionRunResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetAilySessionRunResponse = JSON.unmarshal(str(resp.content, UTF_8), GetAilySessionRunResponse)
        response.raw = resp

        return response

    def list(self, request: ListAilySessionRunRequest,
             option: Optional[RequestOption] = None) -> ListAilySessionRunResponse:
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
        response: ListAilySessionRunResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAilySessionRunResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListAilySessionRunRequest,
                    option: Optional[RequestOption] = None) -> ListAilySessionRunResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListAilySessionRunResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAilySessionRunResponse)
        response.raw = resp

        return response
