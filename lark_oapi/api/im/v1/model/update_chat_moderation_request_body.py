# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class UpdateChatModerationRequestBody(object):
    _types = {
        "moderation_setting": str,
        "moderator_added_list": List[str],
        "moderator_removed_list": List[str],
    }

    def __init__(self, d):
        self.moderation_setting: Optional[str] = None
        self.moderator_added_list: Optional[List[str]] = None
        self.moderator_removed_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateChatModerationRequestBodyBuilder":
        return UpdateChatModerationRequestBodyBuilder()


class UpdateChatModerationRequestBodyBuilder(object):
    def __init__(self, update_chat_moderation_request_body: UpdateChatModerationRequestBody = UpdateChatModerationRequestBody({})) -> None:
        self._update_chat_moderation_request_body: UpdateChatModerationRequestBody = update_chat_moderation_request_body
    
    def moderation_setting(self, moderation_setting: str) -> "UpdateChatModerationRequestBodyBuilder":
        self._update_chat_moderation_request_body.moderation_setting = moderation_setting
        return self
    
    def moderator_added_list(self, moderator_added_list: List[str]) -> "UpdateChatModerationRequestBodyBuilder":
        self._update_chat_moderation_request_body.moderator_added_list = moderator_added_list
        return self
    
    def moderator_removed_list(self, moderator_removed_list: List[str]) -> "UpdateChatModerationRequestBodyBuilder":
        self._update_chat_moderation_request_body.moderator_removed_list = moderator_removed_list
        return self
    
    def build(self) -> "UpdateChatModerationRequestBody":
        return self._update_chat_moderation_request_body