# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class BatchMessageSendProgress(object):
    _types = {
        "valid_user_ids_count": int,
        "success_user_ids_count": int,
        "read_user_ids_count": int,
    }

    def __init__(self, d):
        self.valid_user_ids_count: Optional[int] = None
        self.success_user_ids_count: Optional[int] = None
        self.read_user_ids_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchMessageSendProgressBuilder":
        return BatchMessageSendProgressBuilder()


class BatchMessageSendProgressBuilder(object):
    def __init__(self, batch_message_send_progress: BatchMessageSendProgress = BatchMessageSendProgress({})) -> None:
        self._batch_message_send_progress: BatchMessageSendProgress = batch_message_send_progress
    
    def valid_user_ids_count(self, valid_user_ids_count: int) -> "BatchMessageSendProgressBuilder":
        self._batch_message_send_progress.valid_user_ids_count = valid_user_ids_count
        return self
    
    def success_user_ids_count(self, success_user_ids_count: int) -> "BatchMessageSendProgressBuilder":
        self._batch_message_send_progress.success_user_ids_count = success_user_ids_count
        return self
    
    def read_user_ids_count(self, read_user_ids_count: int) -> "BatchMessageSendProgressBuilder":
        self._batch_message_send_progress.read_user_ids_count = read_user_ids_count
        return self
    
    def build(self) -> "BatchMessageSendProgress":
        return self._batch_message_send_progress