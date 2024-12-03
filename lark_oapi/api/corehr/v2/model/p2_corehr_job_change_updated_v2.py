# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2CorehrJobChangeUpdatedV2Data(object):
    _types = {
        "employment_id": str,
        "tenant_id": str,
        "process_id": str,
        "initiator": str,
        "operator": str,
        "updated_time": str,
        "job_change_id": str,
        "status": int,
        "operate_reason": str,
        "transfer_type": int,
        "updated_fields": List[str],
        "transform_type": str,
        "transform_reason": str,
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.tenant_id: Optional[str] = None
        self.process_id: Optional[str] = None
        self.initiator: Optional[str] = None
        self.operator: Optional[str] = None
        self.updated_time: Optional[str] = None
        self.job_change_id: Optional[str] = None
        self.status: Optional[int] = None
        self.operate_reason: Optional[str] = None
        self.transfer_type: Optional[int] = None
        self.updated_fields: Optional[List[str]] = None
        self.transform_type: Optional[str] = None
        self.transform_reason: Optional[str] = None
        init(self, d, self._types)


class P2CorehrJobChangeUpdatedV2(EventContext):
    _types = {
        "event": P2CorehrJobChangeUpdatedV2Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrJobChangeUpdatedV2Data] = None
        init(self, d, self._types)
