import json
import pprint
from operator import itemgetter
import requests


class SuperJobParser:
    URL = "https://api.superjob.ru/2.0/vacancies/?"

    def __init__(self):
        self.__vacancies_list = []

    def __get_request(self, vacancy_title: str, required_city: str, pages_for_parse=1) -> list:
        header = {
            'X-Api-App-Id': 'v3.r.137492499.b16a17e80e37142b49c504ab10c11777ac54cf17.e2b453df3816952a1869d934a67d40454631be46'
        }

        params = {'keywords': vacancy_title.title(),
                  'town': required_city,
                  'count': 100,
                  'page': pages_for_parse,
                  'more': True}

        return requests.get(self.URL, headers=header, params=params).json()['objects']

    def get_vacancies(self, vacancy_title, pages_for_parse=10):
        # pages_for_parse = 1  # пока что так для удобства
        response = []
        for page in range(pages_for_parse):
            print(f"Парсинг страницы {page + 1}", end=": ")
            values = self.get_request(vacancy_title, page)
            print(f"Найдено {len(values)} вакансий")
            response.extend(values)
        return response


class SuperJobVacancy:
    def __init__(self, keyword):
        self.__filename = f'{keyword.title().strip()}.json'

    @property
    def __data_from_json_file(self):
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

    def show_all_vacancies(self):

        prepared_data = []

        for i in self.__data_from_json_file:

            if i['payment_from']:
                salary_from = i['payment_from']
            else:
                salary_from = 'Начальная плата не указана'

            if i['payment_to']:
                salary_to = i['payment_to']
            else:
                salary_to = 'Максимальная плата не указана'

            prepared_data.append(f"ID вакансии: {i['id']}. "
                                 f"Наименование вакансии: {i['profession']}. "
                                 f"Заработная плата({i['currency']}): {salary_from} - {salary_to}. "
                                 f"Ссылка на вакансию: {i['link']}.")

        return '\n'.join(prepared_data)

    def top_ten_by_avg_salary(self):

        leaders_list = []

        for i in self.__data_from_json_file:
            salary_avg = (i['payment_from'] + i['payment_to']) / 2

            if i['payment_from'] == 0 or i['payment_to'] == 0 or i['currency'] != 'rub':
                continue

            else:
                leaders_list.append({"ID вакансии": i['id'],
                                     "Наименование вакансии": i['profession'],
                                     "Средняя заработная плата": salary_avg,
                                     "Ссылка на вакансию": {i['link']}})
        sorted_data = sorted(leaders_list, key=itemgetter("Средняя заработная плата"), reverse=True)
        pprint.pprint(sorted_data[:10], width=110)
