# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2CorehrProcessCcUpdatedV2Data(object):
    _types = {
        "process_id": str,
        "approver_id": str,
        "status": int,
        "biz_type": str,
    }

    def __init__(self, d=None):
        self.process_id: Optional[str] = None
        self.approver_id: Optional[str] = None
        self.status: Optional[int] = None
        self.biz_type: Optional[str] = None
        init(self, d, self._types)


class P2CorehrProcessCcUpdatedV2(EventContext):
    _types = {
        "event": P2CorehrProcessCcUpdatedV2Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrProcessCcUpdatedV2Data] = None
        init(self, d, self._types)
