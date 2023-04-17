from abc import ABC


class AbstractAPIClass(ABC):

    def get_request(self, vacancy_title: str, pages_for_parse: int):
        pass
