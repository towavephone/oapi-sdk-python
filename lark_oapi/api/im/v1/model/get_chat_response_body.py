# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n_names import I18nNames
from .restricted_mode_setting import RestrictedModeSetting


class GetChatResponseBody(object):
    _types = {
        "avatar": str,
        "name": str,
        "description": str,
        "i18n_names": I18nNames,
        "add_member_permission": str,
        "share_card_permission": str,
        "at_all_permission": str,
        "edit_permission": str,
        "owner_id_type": str,
        "owner_id": str,
        "user_manager_id_list": List[str],
        "bot_manager_id_list": List[str],
        "group_message_type": str,
        "chat_mode": str,
        "chat_type": str,
        "chat_tag": str,
        "join_message_visibility": str,
        "leave_message_visibility": str,
        "membership_approval": str,
        "moderation_permission": str,
        "external": bool,
        "tenant_key": str,
        "user_count": str,
        "bot_count": str,
        "restricted_mode_setting": RestrictedModeSetting,
        "urgent_setting": str,
        "video_conference_setting": str,
        "hide_member_count_setting": str,
        "chat_status": str,
    }

    def __init__(self, d=None):
        self.avatar: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.i18n_names: Optional[I18nNames] = None
        self.add_member_permission: Optional[str] = None
        self.share_card_permission: Optional[str] = None
        self.at_all_permission: Optional[str] = None
        self.edit_permission: Optional[str] = None
        self.owner_id_type: Optional[str] = None
        self.owner_id: Optional[str] = None
        self.user_manager_id_list: Optional[List[str]] = None
        self.bot_manager_id_list: Optional[List[str]] = None
        self.group_message_type: Optional[str] = None
        self.chat_mode: Optional[str] = None
        self.chat_type: Optional[str] = None
        self.chat_tag: Optional[str] = None
        self.join_message_visibility: Optional[str] = None
        self.leave_message_visibility: Optional[str] = None
        self.membership_approval: Optional[str] = None
        self.moderation_permission: Optional[str] = None
        self.external: Optional[bool] = None
        self.tenant_key: Optional[str] = None
        self.user_count: Optional[str] = None
        self.bot_count: Optional[str] = None
        self.restricted_mode_setting: Optional[RestrictedModeSetting] = None
        self.urgent_setting: Optional[str] = None
        self.video_conference_setting: Optional[str] = None
        self.hide_member_count_setting: Optional[str] = None
        self.chat_status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetChatResponseBodyBuilder":
        return GetChatResponseBodyBuilder()


class GetChatResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_chat_response_body = GetChatResponseBody()

    def avatar(self, avatar: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.avatar = avatar
        return self

    def name(self, name: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.name = name
        return self

    def description(self, description: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.description = description
        return self

    def i18n_names(self, i18n_names: I18nNames) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.i18n_names = i18n_names
        return self

    def add_member_permission(self, add_member_permission: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.add_member_permission = add_member_permission
        return self

    def share_card_permission(self, share_card_permission: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.share_card_permission = share_card_permission
        return self

    def at_all_permission(self, at_all_permission: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.at_all_permission = at_all_permission
        return self

    def edit_permission(self, edit_permission: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.edit_permission = edit_permission
        return self

    def owner_id_type(self, owner_id_type: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.owner_id_type = owner_id_type
        return self

    def owner_id(self, owner_id: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.owner_id = owner_id
        return self

    def user_manager_id_list(self, user_manager_id_list: List[str]) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.user_manager_id_list = user_manager_id_list
        return self

    def bot_manager_id_list(self, bot_manager_id_list: List[str]) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.bot_manager_id_list = bot_manager_id_list
        return self

    def group_message_type(self, group_message_type: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.group_message_type = group_message_type
        return self

    def chat_mode(self, chat_mode: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.chat_mode = chat_mode
        return self

    def chat_type(self, chat_type: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.chat_type = chat_type
        return self

    def chat_tag(self, chat_tag: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.chat_tag = chat_tag
        return self

    def join_message_visibility(self, join_message_visibility: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.join_message_visibility = join_message_visibility
        return self

    def leave_message_visibility(self, leave_message_visibility: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.leave_message_visibility = leave_message_visibility
        return self

    def membership_approval(self, membership_approval: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.membership_approval = membership_approval
        return self

    def moderation_permission(self, moderation_permission: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.moderation_permission = moderation_permission
        return self

    def external(self, external: bool) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.external = external
        return self

    def tenant_key(self, tenant_key: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.tenant_key = tenant_key
        return self

    def user_count(self, user_count: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.user_count = user_count
        return self

    def bot_count(self, bot_count: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.bot_count = bot_count
        return self

    def restricted_mode_setting(self, restricted_mode_setting: RestrictedModeSetting) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.restricted_mode_setting = restricted_mode_setting
        return self

    def urgent_setting(self, urgent_setting: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.urgent_setting = urgent_setting
        return self

    def video_conference_setting(self, video_conference_setting: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.video_conference_setting = video_conference_setting
        return self

    def hide_member_count_setting(self, hide_member_count_setting: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.hide_member_count_setting = hide_member_count_setting
        return self

    def chat_status(self, chat_status: str) -> "GetChatResponseBodyBuilder":
        self._get_chat_response_body.chat_status = chat_status
        return self

    def build(self) -> "GetChatResponseBody":
        return self._get_chat_response_body
