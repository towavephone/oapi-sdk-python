# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ChatAnnouncement(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatAnnouncementBuilder":
        return ChatAnnouncementBuilder()


class ChatAnnouncementBuilder(object):
    def __init__(self, chat_announcement: ChatAnnouncement = ChatAnnouncement({})) -> None:
        self._chat_announcement: ChatAnnouncement = chat_announcement
    
    def build(self) -> "ChatAnnouncement":
        return self._chat_announcement