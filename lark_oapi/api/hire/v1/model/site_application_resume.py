# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .site_resume_education import SiteResumeEducation
from .site_resume_career import SiteResumeCareer
from .site_resume_project import SiteResumeProject
from .site_resume_internship import SiteResumeInternship
from .site_resume_work import SiteResumeWork
from .site_resume_award import SiteResumeAward
from .site_resume_language_skill import SiteResumeLanguageSkill
from .site_resume_sns import SiteResumeSns
from .site_resume_identification import SiteResumeIdentification
from .site_resume_competition import SiteResumeCompetition
from .site_resume_certificate import SiteResumeCertificate


class SiteApplicationResume(object):
    _types = {
        "name": str,
        "mobile_number": str,
        "moblie_code": str,
        "email": str,
        "site_attachment_id": str,
        "self_evaluation": str,
        "age": str,
        "working_year": str,
        "education_list": List[SiteResumeEducation],
        "career_list": List[SiteResumeCareer],
        "project_list": List[SiteResumeProject],
        "internship_list": List[SiteResumeInternship],
        "work_list": List[SiteResumeWork],
        "award_list": List[SiteResumeAward],
        "language_skill_list": List[SiteResumeLanguageSkill],
        "sns_list": List[SiteResumeSns],
        "identification": SiteResumeIdentification,
        "competition_list": List[SiteResumeCompetition],
        "certificate_list": List[SiteResumeCertificate],
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        self.mobile_number: Optional[str] = None
        self.moblie_code: Optional[str] = None
        self.email: Optional[str] = None
        self.site_attachment_id: Optional[str] = None
        self.self_evaluation: Optional[str] = None
        self.age: Optional[str] = None
        self.working_year: Optional[str] = None
        self.education_list: Optional[List[SiteResumeEducation]] = None
        self.career_list: Optional[List[SiteResumeCareer]] = None
        self.project_list: Optional[List[SiteResumeProject]] = None
        self.internship_list: Optional[List[SiteResumeInternship]] = None
        self.work_list: Optional[List[SiteResumeWork]] = None
        self.award_list: Optional[List[SiteResumeAward]] = None
        self.language_skill_list: Optional[List[SiteResumeLanguageSkill]] = None
        self.sns_list: Optional[List[SiteResumeSns]] = None
        self.identification: Optional[SiteResumeIdentification] = None
        self.competition_list: Optional[List[SiteResumeCompetition]] = None
        self.certificate_list: Optional[List[SiteResumeCertificate]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteApplicationResumeBuilder":
        return SiteApplicationResumeBuilder()


class SiteApplicationResumeBuilder(object):
    def __init__(self, site_application_resume: SiteApplicationResume = SiteApplicationResume({})) -> None:
        self._site_application_resume: SiteApplicationResume = site_application_resume
    
    def name(self, name: str) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.name = name
        return self
    
    def mobile_number(self, mobile_number: str) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.mobile_number = mobile_number
        return self
    
    def moblie_code(self, moblie_code: str) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.moblie_code = moblie_code
        return self
    
    def email(self, email: str) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.email = email
        return self
    
    def site_attachment_id(self, site_attachment_id: str) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.site_attachment_id = site_attachment_id
        return self
    
    def self_evaluation(self, self_evaluation: str) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.self_evaluation = self_evaluation
        return self
    
    def age(self, age: str) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.age = age
        return self
    
    def working_year(self, working_year: str) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.working_year = working_year
        return self
    
    def education_list(self, education_list: List[SiteResumeEducation]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.education_list = education_list
        return self
    
    def career_list(self, career_list: List[SiteResumeCareer]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.career_list = career_list
        return self
    
    def project_list(self, project_list: List[SiteResumeProject]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.project_list = project_list
        return self
    
    def internship_list(self, internship_list: List[SiteResumeInternship]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.internship_list = internship_list
        return self
    
    def work_list(self, work_list: List[SiteResumeWork]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.work_list = work_list
        return self
    
    def award_list(self, award_list: List[SiteResumeAward]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.award_list = award_list
        return self
    
    def language_skill_list(self, language_skill_list: List[SiteResumeLanguageSkill]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.language_skill_list = language_skill_list
        return self
    
    def sns_list(self, sns_list: List[SiteResumeSns]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.sns_list = sns_list
        return self
    
    def identification(self, identification: SiteResumeIdentification) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.identification = identification
        return self
    
    def competition_list(self, competition_list: List[SiteResumeCompetition]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.competition_list = competition_list
        return self
    
    def certificate_list(self, certificate_list: List[SiteResumeCertificate]) -> "SiteApplicationResumeBuilder":
        self._site_application_resume.certificate_list = certificate_list
        return self
    
    def build(self) -> "SiteApplicationResume":
        return self._site_application_resume