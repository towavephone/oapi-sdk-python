# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ConnectorLogData(object):
    _types = {
        "date_time": str,
        "data": str,
        "level": str,
        "pod": str,
        "location": str,
        "type": str,
        "version": str,
    }

    def __init__(self, d):
        self.date_time: Optional[str] = None
        self.data: Optional[str] = None
        self.level: Optional[str] = None
        self.pod: Optional[str] = None
        self.location: Optional[str] = None
        self.type: Optional[str] = None
        self.version: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ConnectorLogDataBuilder":
        return ConnectorLogDataBuilder()


class ConnectorLogDataBuilder(object):
    def __init__(self, connector_log_data: ConnectorLogData = ConnectorLogData({})) -> None:
        self._connector_log_data: ConnectorLogData = connector_log_data
    
    def date_time(self, date_time: str) -> "ConnectorLogDataBuilder":
        self._connector_log_data.date_time = date_time
        return self
    
    def data(self, data: str) -> "ConnectorLogDataBuilder":
        self._connector_log_data.data = data
        return self
    
    def level(self, level: str) -> "ConnectorLogDataBuilder":
        self._connector_log_data.level = level
        return self
    
    def pod(self, pod: str) -> "ConnectorLogDataBuilder":
        self._connector_log_data.pod = pod
        return self
    
    def location(self, location: str) -> "ConnectorLogDataBuilder":
        self._connector_log_data.location = location
        return self
    
    def type(self, type: str) -> "ConnectorLogDataBuilder":
        self._connector_log_data.type = type
        return self
    
    def version(self, version: str) -> "ConnectorLogDataBuilder":
        self._connector_log_data.version = version
        return self
    
    def build(self) -> "ConnectorLogData":
        return self._connector_log_data