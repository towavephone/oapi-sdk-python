# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v2.resource import *


class TenantService(object):
    def __init__(self, config: Config) -> None:
        self.v2: V2 = V2(config)


class V2(object):
    def __init__(self, config: Config) -> None:
        self.tenant: Optional[Tenant] = Tenant(config)
        self.tenant_product_assign_info: Optional[TenantProductAssignInfo] = TenantProductAssignInfo(config)