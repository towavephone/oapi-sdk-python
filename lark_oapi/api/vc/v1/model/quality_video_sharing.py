# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class QualityVideoSharing(object):
    _types = {
        "time": str,
        "bitrate_received": str,
        "latency_received": str,
        "jitter_received": str,
        "maximum_resolution_received": str,
        "framerate_received": str,
        "bitrate_sent": str,
        "latency_sent": str,
        "jitter_sent": str,
        "maximum_resolution_sent": str,
        "framerate_sent": str,
    }

    def __init__(self, d):
        self.time: Optional[str] = None
        self.bitrate_received: Optional[str] = None
        self.latency_received: Optional[str] = None
        self.jitter_received: Optional[str] = None
        self.maximum_resolution_received: Optional[str] = None
        self.framerate_received: Optional[str] = None
        self.bitrate_sent: Optional[str] = None
        self.latency_sent: Optional[str] = None
        self.jitter_sent: Optional[str] = None
        self.maximum_resolution_sent: Optional[str] = None
        self.framerate_sent: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QualityVideoSharingBuilder":
        return QualityVideoSharingBuilder()


class QualityVideoSharingBuilder(object):
    def __init__(self, quality_video_sharing: QualityVideoSharing = QualityVideoSharing({})) -> None:
        self._quality_video_sharing: QualityVideoSharing = quality_video_sharing
    
    def time(self, time: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.time = time
        return self
    
    def bitrate_received(self, bitrate_received: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.bitrate_received = bitrate_received
        return self
    
    def latency_received(self, latency_received: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.latency_received = latency_received
        return self
    
    def jitter_received(self, jitter_received: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.jitter_received = jitter_received
        return self
    
    def maximum_resolution_received(self, maximum_resolution_received: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.maximum_resolution_received = maximum_resolution_received
        return self
    
    def framerate_received(self, framerate_received: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.framerate_received = framerate_received
        return self
    
    def bitrate_sent(self, bitrate_sent: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.bitrate_sent = bitrate_sent
        return self
    
    def latency_sent(self, latency_sent: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.latency_sent = latency_sent
        return self
    
    def jitter_sent(self, jitter_sent: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.jitter_sent = jitter_sent
        return self
    
    def maximum_resolution_sent(self, maximum_resolution_sent: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.maximum_resolution_sent = maximum_resolution_sent
        return self
    
    def framerate_sent(self, framerate_sent: str) -> "QualityVideoSharingBuilder":
        self._quality_video_sharing.framerate_sent = framerate_sent
        return self
    
    def build(self) -> "QualityVideoSharing":
        return self._quality_video_sharing