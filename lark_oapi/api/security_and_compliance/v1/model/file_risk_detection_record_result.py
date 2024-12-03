# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FileRiskDetectionRecordResult(object):
    _types = {
        "status": str,
        "risk_tag": str,
    }

    def __init__(self, d=None):
        self.status: Optional[str] = None
        self.risk_tag: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileRiskDetectionRecordResultBuilder":
        return FileRiskDetectionRecordResultBuilder()


class FileRiskDetectionRecordResultBuilder(object):
    def __init__(self) -> None:
        self._file_risk_detection_record_result = FileRiskDetectionRecordResult()

    def status(self, status: str) -> "FileRiskDetectionRecordResultBuilder":
        self._file_risk_detection_record_result.status = status
        return self

    def risk_tag(self, risk_tag: str) -> "FileRiskDetectionRecordResultBuilder":
        self._file_risk_detection_record_result.risk_tag = risk_tag
        return self

    def build(self) -> "FileRiskDetectionRecordResult":
        return self._file_risk_detection_record_result
