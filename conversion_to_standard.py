import json
from abc import ABC, abstractmethod

import requests


class API(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями, в нашем случае HH и SJ
    """

    @abstractmethod
    def get_request(self):
        pass


class HeadHunterAPI(API):
    """
    Класс для работы с сайтом HeadHunter
    """
    __base_url = "https://api.hh.ru/vacancies?only_with_salary=true"

    def __init__(self):
        self.params = None
        self.vacancies = None
        self.response_data = None
        self.response_url = None

    def get_request(self, *args):
        self.params = {'text': args,
                       'page': 1,
                       'per_page': 10
                       }
        self.response_url = requests.get(self.__base_url, params=self.params)
        self.response_data = json.loads(self.response_url.text)
        self.vacancies = self.response_data['items']
        return self.vacancies


class SuperJobAPI(API):
    """
    Класс для работы с сайтом SuperJob
    """

    API_KEY = {
        'X-Api-App-Id': 'v3.r.137492499.b16a17e80e37142b49c504ab10c11777ac54cf17.e2b453df3816952a1869d934a67d40454631be46'
    }

    def __init__(self):
        self.params = None
        self.vacancies = None
        self.response_data = None
        self.response = None
        self.response_url = None

    def get_request(self, *args):
        self.params = [("keywords", [("srws", 1), ("skwc", "particular"), ("keys", args)]),
                       ("period", 7),
                       ("count", 10)]
        self.response_url = 'https://api.superjob.ru/2.0/vacancies'
        self.response = requests.get(self.response_url, headers=self.API_KEY, params=self.params)
        self.response_data = json.loads(self.response.text)
        self.vacancies = self.response_data['objects']
        return self.vacancies
