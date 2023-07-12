# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .i18n_names import I18nNames
from .restricted_mode_setting import RestrictedModeSetting


class CreateChatRequestBody(object):
    _types = {
        "avatar": str,
        "name": str,
        "description": str,
        "i18n_names": I18nNames,
        "owner_id": str,
        "user_id_list": List[str],
        "bot_id_list": List[str],
        "chat_mode": str,
        "chat_type": str,
        "external": bool,
        "join_message_visibility": str,
        "leave_message_visibility": str,
        "membership_approval": str,
        "restricted_mode_setting": RestrictedModeSetting,
    }

    def __init__(self, d):
        self.avatar: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.i18n_names: Optional[I18nNames] = None
        self.owner_id: Optional[str] = None
        self.user_id_list: Optional[List[str]] = None
        self.bot_id_list: Optional[List[str]] = None
        self.chat_mode: Optional[str] = None
        self.chat_type: Optional[str] = None
        self.external: Optional[bool] = None
        self.join_message_visibility: Optional[str] = None
        self.leave_message_visibility: Optional[str] = None
        self.membership_approval: Optional[str] = None
        self.labels: Optional[List[str]] = None
        self.toolkit_ids: Optional[List[int]] = None
        self.restricted_mode_setting: Optional[RestrictedModeSetting] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateChatRequestBodyBuilder":
        return CreateChatRequestBodyBuilder()


class CreateChatRequestBodyBuilder(object):
    def __init__(self, create_chat_request_body: CreateChatRequestBody = CreateChatRequestBody({})) -> None:
        self._create_chat_request_body: CreateChatRequestBody = create_chat_request_body
    
    def avatar(self, avatar: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.avatar = avatar
        return self
    
    def name(self, name: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.name = name
        return self
    
    def description(self, description: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.description = description
        return self
    
    def i18n_names(self, i18n_names: I18nNames) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.i18n_names = i18n_names
        return self
    
    def owner_id(self, owner_id: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.owner_id = owner_id
        return self
    
    def user_id_list(self, user_id_list: List[str]) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.user_id_list = user_id_list
        return self
    
    def bot_id_list(self, bot_id_list: List[str]) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.bot_id_list = bot_id_list
        return self
    
    def chat_mode(self, chat_mode: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.chat_mode = chat_mode
        return self
    
    def chat_type(self, chat_type: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.chat_type = chat_type
        return self
    
    def external(self, external: bool) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.external = external
        return self
    
    def join_message_visibility(self, join_message_visibility: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.join_message_visibility = join_message_visibility
        return self
    
    def leave_message_visibility(self, leave_message_visibility: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.leave_message_visibility = leave_message_visibility
        return self
    
    def membership_approval(self, membership_approval: str) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.membership_approval = membership_approval
        return self
    
    
    
    def restricted_mode_setting(self, restricted_mode_setting: RestrictedModeSetting) -> "CreateChatRequestBodyBuilder":
        self._create_chat_request_body.restricted_mode_setting = restricted_mode_setting
        return self
    
    def build(self) -> "CreateChatRequestBody":
        return self._create_chat_request_body