# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class MetricTable(object):
    _types = {
        "metric_table_id": str,
        "metric_table_name": str,
        "period_id": str,
    }

    def __init__(self, d):
        self.metric_table_id: Optional[str] = None
        self.metric_table_name: Optional[str] = None
        self.period_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MetricTableBuilder":
        return MetricTableBuilder()


class MetricTableBuilder(object):
    def __init__(self, metric_table: MetricTable = MetricTable({})) -> None:
        self._metric_table: MetricTable = metric_table
    
    def metric_table_id(self, metric_table_id: str) -> "MetricTableBuilder":
        self._metric_table.metric_table_id = metric_table_id
        return self
    
    def metric_table_name(self, metric_table_name: str) -> "MetricTableBuilder":
        self._metric_table.metric_table_name = metric_table_name
        return self
    
    def period_id(self, period_id: str) -> "MetricTableBuilder":
        self._metric_table.period_id = period_id
        return self
    
    def build(self) -> "MetricTable":
        return self._metric_table