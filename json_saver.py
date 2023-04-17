import json
from abc import ABC, abstractmethod

from conversion_to_standard import HeadHunterAPI, SuperJobAPI


class JSONSaver(ABC):

    @abstractmethod
    def add_vacancy(self, *args):
        pass


class JSONSaverHH(JSONSaver):

    def __init__(self):
        self.test = None
        self.discharge = None

    def add_vacancy(self, search_word):
        self.discharge = HeadHunterAPI()
        self.test = self.discharge.get_request(search_word)
        with open(f'{search_word}_hh_data.json', 'w', encoding='utf-8') as file:
            json.dump(self.test, file, indent=4, ensure_ascii=False)
            print('Данные успешно записаны!')


class JSONSaverSJ(JSONSaver):

    def __init__(self):
        self.test = None
        self.discharge = None

    def add_vacancy(self, search_word):
        self.discharge = SuperJobAPI()
        self.test = self.discharge.get_request(search_word)
        with open(f'{search_word}_sj_data.json', 'w', encoding='utf-8') as file:
            json.dump(self.test, file, indent=4, ensure_ascii=False)
            print("Данные выгружены")


exp = JSONSaverSJ()
print(exp.add_vacancy('Гинеколог'))
