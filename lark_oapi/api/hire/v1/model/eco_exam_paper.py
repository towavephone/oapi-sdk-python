# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .eco_exam_paper_data import EcoExamPaperData


class EcoExamPaper(object):
    _types = {
        "account_id": str,
        "paper_list": List[EcoExamPaperData],
    }

    def __init__(self, d):
        self.account_id: Optional[str] = None
        self.paper_list: Optional[List[EcoExamPaperData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoExamPaperBuilder":
        return EcoExamPaperBuilder()


class EcoExamPaperBuilder(object):
    def __init__(self, eco_exam_paper: EcoExamPaper = EcoExamPaper({})) -> None:
        self._eco_exam_paper: EcoExamPaper = eco_exam_paper
    
    def account_id(self, account_id: str) -> "EcoExamPaperBuilder":
        self._eco_exam_paper.account_id = account_id
        return self
    
    def paper_list(self, paper_list: List[EcoExamPaperData]) -> "EcoExamPaperBuilder":
        self._eco_exam_paper.paper_list = paper_list
        return self
    
    def build(self) -> "EcoExamPaper":
        return self._eco_exam_paper