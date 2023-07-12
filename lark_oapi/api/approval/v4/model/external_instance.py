# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .external_instance_link import ExternalInstanceLink
from .external_instance_form import ExternalInstanceForm
from .external_instance_task_node import ExternalInstanceTaskNode
from .cc_node import CcNode
from .i18n_resource import I18nResource
from .trusteeship_urls import TrusteeshipUrls
from .trusteeship_instance_cache_config import TrusteeshipInstanceCacheConfig


class ExternalInstance(object):
    _types = {
        "approval_code": str,
        "status": str,
        "extra": str,
        "instance_id": str,
        "links": ExternalInstanceLink,
        "title": str,
        "form": List[ExternalInstanceForm],
        "user_id": str,
        "user_name": str,
        "open_id": str,
        "department_id": str,
        "department_name": str,
        "start_time": int,
        "end_time": int,
        "update_time": int,
        "display_method": str,
        "update_mode": str,
        "task_list": List[ExternalInstanceTaskNode],
        "cc_list": List[CcNode],
        "i18n_resources": List[I18nResource],
        "trusteeship_url_token": str,
        "trusteeship_user_id_type": str,
        "trusteeship_urls": TrusteeshipUrls,
        "trusteeship_cache_config": TrusteeshipInstanceCacheConfig,
    }

    def __init__(self, d):
        self.approval_code: Optional[str] = None
        self.status: Optional[str] = None
        self.extra: Optional[str] = None
        self.instance_id: Optional[str] = None
        self.links: Optional[ExternalInstanceLink] = None
        self.title: Optional[str] = None
        self.form: Optional[List[ExternalInstanceForm]] = None
        self.user_id: Optional[str] = None
        self.user_name: Optional[str] = None
        self.open_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.department_name: Optional[str] = None
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.display_method: Optional[str] = None
        self.update_mode: Optional[str] = None
        self.task_list: Optional[List[ExternalInstanceTaskNode]] = None
        self.cc_list: Optional[List[CcNode]] = None
        self.i18n_resources: Optional[List[I18nResource]] = None
        self.trusteeship_url_token: Optional[str] = None
        self.trusteeship_user_id_type: Optional[str] = None
        self.trusteeship_urls: Optional[TrusteeshipUrls] = None
        self.trusteeship_cache_config: Optional[TrusteeshipInstanceCacheConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalInstanceBuilder":
        return ExternalInstanceBuilder()


class ExternalInstanceBuilder(object):
    def __init__(self, external_instance: ExternalInstance = ExternalInstance({})) -> None:
        self._external_instance: ExternalInstance = external_instance
    
    def approval_code(self, approval_code: str) -> "ExternalInstanceBuilder":
        self._external_instance.approval_code = approval_code
        return self
    
    def status(self, status: str) -> "ExternalInstanceBuilder":
        self._external_instance.status = status
        return self
    
    def extra(self, extra: str) -> "ExternalInstanceBuilder":
        self._external_instance.extra = extra
        return self
    
    def instance_id(self, instance_id: str) -> "ExternalInstanceBuilder":
        self._external_instance.instance_id = instance_id
        return self
    
    def links(self, links: ExternalInstanceLink) -> "ExternalInstanceBuilder":
        self._external_instance.links = links
        return self
    
    def title(self, title: str) -> "ExternalInstanceBuilder":
        self._external_instance.title = title
        return self
    
    def form(self, form: List[ExternalInstanceForm]) -> "ExternalInstanceBuilder":
        self._external_instance.form = form
        return self
    
    def user_id(self, user_id: str) -> "ExternalInstanceBuilder":
        self._external_instance.user_id = user_id
        return self
    
    def user_name(self, user_name: str) -> "ExternalInstanceBuilder":
        self._external_instance.user_name = user_name
        return self
    
    def open_id(self, open_id: str) -> "ExternalInstanceBuilder":
        self._external_instance.open_id = open_id
        return self
    
    def department_id(self, department_id: str) -> "ExternalInstanceBuilder":
        self._external_instance.department_id = department_id
        return self
    
    def department_name(self, department_name: str) -> "ExternalInstanceBuilder":
        self._external_instance.department_name = department_name
        return self
    
    def start_time(self, start_time: int) -> "ExternalInstanceBuilder":
        self._external_instance.start_time = start_time
        return self
    
    def end_time(self, end_time: int) -> "ExternalInstanceBuilder":
        self._external_instance.end_time = end_time
        return self
    
    def update_time(self, update_time: int) -> "ExternalInstanceBuilder":
        self._external_instance.update_time = update_time
        return self
    
    def display_method(self, display_method: str) -> "ExternalInstanceBuilder":
        self._external_instance.display_method = display_method
        return self
    
    def update_mode(self, update_mode: str) -> "ExternalInstanceBuilder":
        self._external_instance.update_mode = update_mode
        return self
    
    def task_list(self, task_list: List[ExternalInstanceTaskNode]) -> "ExternalInstanceBuilder":
        self._external_instance.task_list = task_list
        return self
    
    def cc_list(self, cc_list: List[CcNode]) -> "ExternalInstanceBuilder":
        self._external_instance.cc_list = cc_list
        return self
    
    def i18n_resources(self, i18n_resources: List[I18nResource]) -> "ExternalInstanceBuilder":
        self._external_instance.i18n_resources = i18n_resources
        return self
    
    def trusteeship_url_token(self, trusteeship_url_token: str) -> "ExternalInstanceBuilder":
        self._external_instance.trusteeship_url_token = trusteeship_url_token
        return self
    
    def trusteeship_user_id_type(self, trusteeship_user_id_type: str) -> "ExternalInstanceBuilder":
        self._external_instance.trusteeship_user_id_type = trusteeship_user_id_type
        return self
    
    def trusteeship_urls(self, trusteeship_urls: TrusteeshipUrls) -> "ExternalInstanceBuilder":
        self._external_instance.trusteeship_urls = trusteeship_urls
        return self
    
    def trusteeship_cache_config(self, trusteeship_cache_config: TrusteeshipInstanceCacheConfig) -> "ExternalInstanceBuilder":
        self._external_instance.trusteeship_cache_config = trusteeship_cache_config
        return self
    
    def build(self) -> "ExternalInstance":
        return self._external_instance