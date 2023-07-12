# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .chat_menu_item_redirect_link import ChatMenuItemRedirectLink
from .i18n_names import I18nNames


class ChatMenuItem(object):
    _types = {
        "action_type": str,
        "redirect_link": ChatMenuItemRedirectLink,
        "image_key": str,
        "name": str,
        "i18n_names": I18nNames,
    }

    def __init__(self, d):
        self.action_type: Optional[str] = None
        self.redirect_link: Optional[ChatMenuItemRedirectLink] = None
        self.image_key: Optional[str] = None
        self.name: Optional[str] = None
        self.i18n_names: Optional[I18nNames] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatMenuItemBuilder":
        return ChatMenuItemBuilder()


class ChatMenuItemBuilder(object):
    def __init__(self, chat_menu_item: ChatMenuItem = ChatMenuItem({})) -> None:
        self._chat_menu_item: ChatMenuItem = chat_menu_item
    
    def action_type(self, action_type: str) -> "ChatMenuItemBuilder":
        self._chat_menu_item.action_type = action_type
        return self
    
    def redirect_link(self, redirect_link: ChatMenuItemRedirectLink) -> "ChatMenuItemBuilder":
        self._chat_menu_item.redirect_link = redirect_link
        return self
    
    def image_key(self, image_key: str) -> "ChatMenuItemBuilder":
        self._chat_menu_item.image_key = image_key
        return self
    
    def name(self, name: str) -> "ChatMenuItemBuilder":
        self._chat_menu_item.name = name
        return self
    
    def i18n_names(self, i18n_names: I18nNames) -> "ChatMenuItemBuilder":
        self._chat_menu_item.i18n_names = i18n_names
        return self
    
    def build(self) -> "ChatMenuItem":
        return self._chat_menu_item