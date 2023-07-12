# Code generated by Lark OpenAPI.

import io
from typing import *
from typing import IO
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from lark_oapi.api.drive.v1.model.delete_file_comment_reply_request import DeleteFileCommentReplyRequest
from lark_oapi.api.drive.v1.model.delete_file_comment_reply_response import DeleteFileCommentReplyResponse
from lark_oapi.api.drive.v1.model.update_file_comment_reply_request import UpdateFileCommentReplyRequest
from lark_oapi.api.drive.v1.model.update_file_comment_reply_response import UpdateFileCommentReplyResponse


class FileCommentReply(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def delete(self, request: DeleteFileCommentReplyRequest, option: RequestOption = RequestOption()) -> DeleteFileCommentReplyResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteFileCommentReplyResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteFileCommentReplyResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateFileCommentReplyRequest, option: RequestOption = RequestOption()) -> UpdateFileCommentReplyResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateFileCommentReplyResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateFileCommentReplyResponse)
        response.raw = resp

        return response

    
