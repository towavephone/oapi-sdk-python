# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_employees_additional_job_response_body import PatchEmployeesAdditionalJobResponseBody


class PatchEmployeesAdditionalJobResponse(BaseResponse):
    _types = {
        "data": PatchEmployeesAdditionalJobResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchEmployeesAdditionalJobResponseBody] = None
        init(self, d, self._types)
