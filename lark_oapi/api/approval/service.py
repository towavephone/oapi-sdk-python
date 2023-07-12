# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v4.resource import *


class ApprovalService(object):
    def __init__(self, config: Config) -> None:
        self.v4: V4 = V4(config)


class V4(object):
    def __init__(self, config: Config) -> None:
        self.approval: Optional[Approval] = Approval(config)
        self.external_approval: Optional[ExternalApproval] = ExternalApproval(config)
        self.external_instance: Optional[ExternalInstance] = ExternalInstance(config)
        self.external_task: Optional[ExternalTask] = ExternalTask(config)
        self.instance: Optional[Instance] = Instance(config)
        self.instance_comment: Optional[InstanceComment] = InstanceComment(config)
        self.task: Optional[Task] = Task(config)