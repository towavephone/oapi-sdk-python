# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .support_cost_center_item import SupportCostCenterItem
from .support_cost_center_item import SupportCostCenterItem


class TransferInfo(object):
    _types = {
        "remark": str,
        "offer_info": str,
        "target_dotted_manager_clean": bool,
        "probation_exist": bool,
        "original_department": str,
        "target_department": str,
        "original_work_location": str,
        "target_work_location": str,
        "original_direct_manager": str,
        "target_direct_manager": str,
        "original_dotted_manager": str,
        "target_dotted_manager": str,
        "original_job": str,
        "target_job": str,
        "original_job_family": str,
        "target_job_family": str,
        "original_job_level": str,
        "target_job_level": str,
        "original_workforce_type": str,
        "target_workforce_type": str,
        "original_company": str,
        "target_company": str,
        "original_contract_number": str,
        "target_contract_number": str,
        "original_contract_type": str,
        "target_contract_type": str,
        "original_duration_type": str,
        "target_duration_type": str,
        "original_signing_type": str,
        "target_signing_type": str,
        "original_contract_start_date": str,
        "target_contract_start_date": str,
        "original_contract_end_date": str,
        "target_contract_end_date": str,
        "original_working_hours_type": str,
        "target_working_hours_type": str,
        "original_working_calendar": str,
        "target_working_calendar": str,
        "original_probation_end_date": str,
        "target_probation_end_date": str,
        "original_weekly_working_hours": str,
        "target_weekly_working_hours": str,
        "original_work_shift": str,
        "target_work_shift": str,
        "original_cost_center_rate": List[SupportCostCenterItem],
        "target_cost_center_rate": List[SupportCostCenterItem],
    }

    def __init__(self, d):
        self.remark: Optional[str] = None
        self.offer_info: Optional[str] = None
        self.target_dotted_manager_clean: Optional[bool] = None
        self.probation_exist: Optional[bool] = None
        self.original_department: Optional[str] = None
        self.target_department: Optional[str] = None
        self.original_work_location: Optional[str] = None
        self.target_work_location: Optional[str] = None
        self.original_direct_manager: Optional[str] = None
        self.target_direct_manager: Optional[str] = None
        self.original_dotted_manager: Optional[str] = None
        self.target_dotted_manager: Optional[str] = None
        self.original_job: Optional[str] = None
        self.target_job: Optional[str] = None
        self.original_job_family: Optional[str] = None
        self.target_job_family: Optional[str] = None
        self.original_job_level: Optional[str] = None
        self.target_job_level: Optional[str] = None
        self.original_workforce_type: Optional[str] = None
        self.target_workforce_type: Optional[str] = None
        self.original_company: Optional[str] = None
        self.target_company: Optional[str] = None
        self.original_contract_number: Optional[str] = None
        self.target_contract_number: Optional[str] = None
        self.original_contract_type: Optional[str] = None
        self.target_contract_type: Optional[str] = None
        self.original_duration_type: Optional[str] = None
        self.target_duration_type: Optional[str] = None
        self.original_signing_type: Optional[str] = None
        self.target_signing_type: Optional[str] = None
        self.original_contract_start_date: Optional[str] = None
        self.target_contract_start_date: Optional[str] = None
        self.original_contract_end_date: Optional[str] = None
        self.target_contract_end_date: Optional[str] = None
        self.original_working_hours_type: Optional[str] = None
        self.target_working_hours_type: Optional[str] = None
        self.original_working_calendar: Optional[str] = None
        self.target_working_calendar: Optional[str] = None
        self.original_probation_end_date: Optional[str] = None
        self.target_probation_end_date: Optional[str] = None
        self.original_weekly_working_hours: Optional[str] = None
        self.target_weekly_working_hours: Optional[str] = None
        self.original_work_shift: Optional[str] = None
        self.target_work_shift: Optional[str] = None
        self.original_cost_center_rate: Optional[List[SupportCostCenterItem]] = None
        self.target_cost_center_rate: Optional[List[SupportCostCenterItem]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TransferInfoBuilder":
        return TransferInfoBuilder()


class TransferInfoBuilder(object):
    def __init__(self, transfer_info: TransferInfo = TransferInfo({})) -> None:
        self._transfer_info: TransferInfo = transfer_info
    
    def remark(self, remark: str) -> "TransferInfoBuilder":
        self._transfer_info.remark = remark
        return self
    
    def offer_info(self, offer_info: str) -> "TransferInfoBuilder":
        self._transfer_info.offer_info = offer_info
        return self
    
    def target_dotted_manager_clean(self, target_dotted_manager_clean: bool) -> "TransferInfoBuilder":
        self._transfer_info.target_dotted_manager_clean = target_dotted_manager_clean
        return self
    
    def probation_exist(self, probation_exist: bool) -> "TransferInfoBuilder":
        self._transfer_info.probation_exist = probation_exist
        return self
    
    def original_department(self, original_department: str) -> "TransferInfoBuilder":
        self._transfer_info.original_department = original_department
        return self
    
    def target_department(self, target_department: str) -> "TransferInfoBuilder":
        self._transfer_info.target_department = target_department
        return self
    
    def original_work_location(self, original_work_location: str) -> "TransferInfoBuilder":
        self._transfer_info.original_work_location = original_work_location
        return self
    
    def target_work_location(self, target_work_location: str) -> "TransferInfoBuilder":
        self._transfer_info.target_work_location = target_work_location
        return self
    
    def original_direct_manager(self, original_direct_manager: str) -> "TransferInfoBuilder":
        self._transfer_info.original_direct_manager = original_direct_manager
        return self
    
    def target_direct_manager(self, target_direct_manager: str) -> "TransferInfoBuilder":
        self._transfer_info.target_direct_manager = target_direct_manager
        return self
    
    def original_dotted_manager(self, original_dotted_manager: str) -> "TransferInfoBuilder":
        self._transfer_info.original_dotted_manager = original_dotted_manager
        return self
    
    def target_dotted_manager(self, target_dotted_manager: str) -> "TransferInfoBuilder":
        self._transfer_info.target_dotted_manager = target_dotted_manager
        return self
    
    def original_job(self, original_job: str) -> "TransferInfoBuilder":
        self._transfer_info.original_job = original_job
        return self
    
    def target_job(self, target_job: str) -> "TransferInfoBuilder":
        self._transfer_info.target_job = target_job
        return self
    
    def original_job_family(self, original_job_family: str) -> "TransferInfoBuilder":
        self._transfer_info.original_job_family = original_job_family
        return self
    
    def target_job_family(self, target_job_family: str) -> "TransferInfoBuilder":
        self._transfer_info.target_job_family = target_job_family
        return self
    
    def original_job_level(self, original_job_level: str) -> "TransferInfoBuilder":
        self._transfer_info.original_job_level = original_job_level
        return self
    
    def target_job_level(self, target_job_level: str) -> "TransferInfoBuilder":
        self._transfer_info.target_job_level = target_job_level
        return self
    
    def original_workforce_type(self, original_workforce_type: str) -> "TransferInfoBuilder":
        self._transfer_info.original_workforce_type = original_workforce_type
        return self
    
    def target_workforce_type(self, target_workforce_type: str) -> "TransferInfoBuilder":
        self._transfer_info.target_workforce_type = target_workforce_type
        return self
    
    def original_company(self, original_company: str) -> "TransferInfoBuilder":
        self._transfer_info.original_company = original_company
        return self
    
    def target_company(self, target_company: str) -> "TransferInfoBuilder":
        self._transfer_info.target_company = target_company
        return self
    
    def original_contract_number(self, original_contract_number: str) -> "TransferInfoBuilder":
        self._transfer_info.original_contract_number = original_contract_number
        return self
    
    def target_contract_number(self, target_contract_number: str) -> "TransferInfoBuilder":
        self._transfer_info.target_contract_number = target_contract_number
        return self
    
    def original_contract_type(self, original_contract_type: str) -> "TransferInfoBuilder":
        self._transfer_info.original_contract_type = original_contract_type
        return self
    
    def target_contract_type(self, target_contract_type: str) -> "TransferInfoBuilder":
        self._transfer_info.target_contract_type = target_contract_type
        return self
    
    def original_duration_type(self, original_duration_type: str) -> "TransferInfoBuilder":
        self._transfer_info.original_duration_type = original_duration_type
        return self
    
    def target_duration_type(self, target_duration_type: str) -> "TransferInfoBuilder":
        self._transfer_info.target_duration_type = target_duration_type
        return self
    
    def original_signing_type(self, original_signing_type: str) -> "TransferInfoBuilder":
        self._transfer_info.original_signing_type = original_signing_type
        return self
    
    def target_signing_type(self, target_signing_type: str) -> "TransferInfoBuilder":
        self._transfer_info.target_signing_type = target_signing_type
        return self
    
    def original_contract_start_date(self, original_contract_start_date: str) -> "TransferInfoBuilder":
        self._transfer_info.original_contract_start_date = original_contract_start_date
        return self
    
    def target_contract_start_date(self, target_contract_start_date: str) -> "TransferInfoBuilder":
        self._transfer_info.target_contract_start_date = target_contract_start_date
        return self
    
    def original_contract_end_date(self, original_contract_end_date: str) -> "TransferInfoBuilder":
        self._transfer_info.original_contract_end_date = original_contract_end_date
        return self
    
    def target_contract_end_date(self, target_contract_end_date: str) -> "TransferInfoBuilder":
        self._transfer_info.target_contract_end_date = target_contract_end_date
        return self
    
    def original_working_hours_type(self, original_working_hours_type: str) -> "TransferInfoBuilder":
        self._transfer_info.original_working_hours_type = original_working_hours_type
        return self
    
    def target_working_hours_type(self, target_working_hours_type: str) -> "TransferInfoBuilder":
        self._transfer_info.target_working_hours_type = target_working_hours_type
        return self
    
    def original_working_calendar(self, original_working_calendar: str) -> "TransferInfoBuilder":
        self._transfer_info.original_working_calendar = original_working_calendar
        return self
    
    def target_working_calendar(self, target_working_calendar: str) -> "TransferInfoBuilder":
        self._transfer_info.target_working_calendar = target_working_calendar
        return self
    
    def original_probation_end_date(self, original_probation_end_date: str) -> "TransferInfoBuilder":
        self._transfer_info.original_probation_end_date = original_probation_end_date
        return self
    
    def target_probation_end_date(self, target_probation_end_date: str) -> "TransferInfoBuilder":
        self._transfer_info.target_probation_end_date = target_probation_end_date
        return self
    
    def original_weekly_working_hours(self, original_weekly_working_hours: str) -> "TransferInfoBuilder":
        self._transfer_info.original_weekly_working_hours = original_weekly_working_hours
        return self
    
    def target_weekly_working_hours(self, target_weekly_working_hours: str) -> "TransferInfoBuilder":
        self._transfer_info.target_weekly_working_hours = target_weekly_working_hours
        return self
    
    def original_work_shift(self, original_work_shift: str) -> "TransferInfoBuilder":
        self._transfer_info.original_work_shift = original_work_shift
        return self
    
    def target_work_shift(self, target_work_shift: str) -> "TransferInfoBuilder":
        self._transfer_info.target_work_shift = target_work_shift
        return self
    
    def original_cost_center_rate(self, original_cost_center_rate: List[SupportCostCenterItem]) -> "TransferInfoBuilder":
        self._transfer_info.original_cost_center_rate = original_cost_center_rate
        return self
    
    def target_cost_center_rate(self, target_cost_center_rate: List[SupportCostCenterItem]) -> "TransferInfoBuilder":
        self._transfer_info.target_cost_center_rate = target_cost_center_rate
        return self
    
    def build(self) -> "TransferInfo":
        return self._transfer_info