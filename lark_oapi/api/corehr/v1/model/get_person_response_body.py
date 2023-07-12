# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .person import Person


class GetPersonResponseBody(object):
    _types = {
        "person": Person,
    }

    def __init__(self, d):
        self.person: Optional[Person] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetPersonResponseBodyBuilder":
        return GetPersonResponseBodyBuilder()


class GetPersonResponseBodyBuilder(object):
    def __init__(self, get_person_response_body: GetPersonResponseBody = GetPersonResponseBody({})) -> None:
        self._get_person_response_body: GetPersonResponseBody = get_person_response_body
    
    def person(self, person: Person) -> "GetPersonResponseBodyBuilder":
        self._get_person_response_body.person = person
        return self
    
    def build(self) -> "GetPersonResponseBody":
        return self._get_person_response_body