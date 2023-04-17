import json
from operator import itemgetter

import requests
from pprint import pprint

from AbstractCLS import AbstractAPIClass


class HeadHunterAPI(AbstractAPIClass):
    __base_url = "https://api.hh.ru/vacancies?only_with_salary=true"

    def get_request(self, vacancy_title, pages_for_parse):
        params = {
            "keyword": vacancy_title,
            "page": pages_for_parse,
            "per_page": 100,
        }
        return requests.get(self.__base_url, params=params).json()["items"]

    def get_vacancies(self, vacancy_title, pages_for_parse=10):
        pages_for_parse = 1  # пока что так для удобства
        response = []
        for page in range(pages_for_parse):
            print(f"Парсинг страницы {page + 1}", end=": ")
            values = self.get_request(vacancy_title, page)
            print(f"Найдено {len(values)} вакансий")
            response.extend(values)
        return response


# class Vacancy:
#     __slots__ = ('title', 'salary_min', 'salary_max', 'employee', 'link')
#
#     def __init__(self, title, salary_min, salary_max, employee, link):
#         self.title = title
#         self.salary_min = salary_min
#         self.salary_max = salary_max
#         self.employee = employee
#         self.link = link


class HeadHunterVacancy:
    def __init__(self, keyword: str):
        self.__filename = f'{keyword.title().strip()}.json'

    @property
    def data_from_json_file(self):
        """
        Метод для получения данных из записанного JSON файла.
        Метод служит для облегчения интерфейса класса
        """
        with open(self.__filename, encoding='utf-8') as file:
            vacancies = json.load(file)
            return vacancies

    def write_to_json_file(self, data):
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def show_all_vacancies(self) -> str:
        """Метод для вывода краткой информации о всех собранных вакансиях"""

        prepared_data = []

        for i in self.data_from_json_file:
            salary_from = 'Начальная плата не указана' if not i['salary'].get('from') else i['salary'].get('from')
            salary_to = 'Максимальный порог не указан' if not i['salary'].get('to') else i['salary'].get('to')

            prepared_data.append(f"ID вакансии: {i['id']}. "
                               f"Наименование вакансии: {i['name']}. "
                               f"Заработная плата({i['salary']['currency']}): {salary_from} - {salary_to}. "
                               f"Ссылка на вакансию: {i['alternate_url']}.")

        return '\n'.join(prepared_data)

    def top_ten_by_avg_salary(self):
        """
        Метод для вывода информации о топ 10 вакансиях по заработной плате.
        Метод выводит только те вакансии, в которых заработная плата указана в рублях
        """
        leaders_list = []

        for i in self.data_from_json_file:
            if i['salary']['from'] is None or i['salary']['to'] is None or i['salary']['currency'] != 'RUR':
                continue

            else:
                salary_avg = (i['salary']['from'] + i['salary']['to']) / 2
                leaders_list.append({"ID вакансии": i['id'],
                                     "Наименование вакансии": i['name'],
                                     "Средняя заработная плата": salary_avg,
                                     "Ссылка на вакансию": {i['alternate_url']}})
        sorted_data = sorted(leaders_list, key=itemgetter("Средняя заработная плата"), reverse=True)
        pprint(sorted_data[:10], width=110)
