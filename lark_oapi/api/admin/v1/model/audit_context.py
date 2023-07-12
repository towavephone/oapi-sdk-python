# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .audit_ios_context import AuditIosContext
from .audit_pc_context import AuditPcContext
from .audit_web_context import AuditWebContext
from .audit_android_context import AuditAndroidContext


class AuditContext(object):
    _types = {
        "terminal_type": int,
        "ios_context": AuditIosContext,
        "pc_context": AuditPcContext,
        "web_context": AuditWebContext,
        "android_context": AuditAndroidContext,
    }

    def __init__(self, d):
        self.terminal_type: Optional[int] = None
        self.ios_context: Optional[AuditIosContext] = None
        self.pc_context: Optional[AuditPcContext] = None
        self.web_context: Optional[AuditWebContext] = None
        self.android_context: Optional[AuditAndroidContext] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AuditContextBuilder":
        return AuditContextBuilder()


class AuditContextBuilder(object):
    def __init__(self, audit_context: AuditContext = AuditContext({})) -> None:
        self._audit_context: AuditContext = audit_context
    
    def terminal_type(self, terminal_type: int) -> "AuditContextBuilder":
        self._audit_context.terminal_type = terminal_type
        return self
    
    def ios_context(self, ios_context: AuditIosContext) -> "AuditContextBuilder":
        self._audit_context.ios_context = ios_context
        return self
    
    def pc_context(self, pc_context: AuditPcContext) -> "AuditContextBuilder":
        self._audit_context.pc_context = pc_context
        return self
    
    def web_context(self, web_context: AuditWebContext) -> "AuditContextBuilder":
        self._audit_context.web_context = web_context
        return self
    
    def android_context(self, android_context: AuditAndroidContext) -> "AuditContextBuilder":
        self._audit_context.android_context = android_context
        return self
    
    def build(self) -> "AuditContext":
        return self._audit_context