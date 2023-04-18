import json

from sort_funcs import sort_by_max_salary_hh, sort_by_max_salary_sj


class HeadHunterVacancy:
    """
    Класс для определения вакансий с hh
    """

    def __init__(self):
        self.sorted_list = None
        self.vacancy_hh = None
        self.vacancy = None

    def show_all_vacancies(self):
        """
        Метод выводит вакансии и информацию о компании, зарплате, должности из файла
        """

        with open('hh_Data.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            self.vacancy_hh = sort_by_max_salary_hh(self.vacancy)
            for vacancy in self.vacancy_hh:
                if vacancy['salary']['currency'] != 'RUR':
                    continue
                if vacancy['salary']['from'] is None:
                    vacancy['salary']['from'] = 'Начальная плата не указана'
                else:
                    vacancy['salary']['from'] = vacancy['salary']['from']
                if vacancy['salary']['to'] is None:
                    vacancy['salary']['to'] = 'Максимальный порог не указан'
                else:
                    vacancy['salary']['to'] = vacancy['salary']['to']

                print(f"Название организации: {vacancy['employer']['name']}.\n"
                      f"Наименование вакансии: {vacancy['name']}.\n"
                      f"Заработная плата({vacancy['salary']['currency']}): {vacancy['salary']['from']} - {vacancy['salary']['to']}.\n"
                      f"Ссылка на вакансию: {vacancy['alternate_url']}.\n")

    def top_by_avg_salary(self):
        """
        Метод сортирует вакансии в соответствии с максимальной зарплатой
        """

        leaders_list = []
        with open('hh_Data.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            for i in self.vacancy:
                if i['salary']['from'] is None or i['salary']['to'] is None or i['salary']['currency'] != 'RUR':
                    continue
                leaders_list.append(i)
        self.sorted_list = sorted(leaders_list, key=lambda data: (data["salary"]["to"]),
                                  reverse=True)[:10]
        for vacancy in self.sorted_list:
            print(f"Название организации: {vacancy['employer']['name']}.\n"
                  f"Наименование вакансии: {vacancy['name']}.\n"
                  f"Заработная плата({vacancy['salary']['currency']}): {vacancy['salary']['from']} - {vacancy['salary']['to']}.\n"
                  f"Ссылка на вакансию: {vacancy['alternate_url']}.\n")


class SuperJobVacancy:
    """
    Класс для определения вакансий с sj
    """

    def __init__(self):
        self.sorted_list = None
        self.vacancy_sj = None
        self.vacancy = None

    def show_all_vacancies(self):
        """
        Метод выводит вакансии и информацию о компании, зарплате, должности из файла
        """

        with open('sj_Data.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            self.vacancy_sj = sort_by_max_salary_sj(self.vacancy)
            for vacancy in self.vacancy_sj:
                if vacancy['payment_from'] == 0:
                    vacancy['payment_from'] = 'Начальная плата не указана'
                if vacancy['payment_to'] == 0:
                    vacancy['payment_to'] = 'Максимальный порог не указан'

                print(f"Название организации: {vacancy['firm_name']}.\n"
                      f"Наименование вакансии: {vacancy['profession']}.\n"
                      f"Заработная плата({vacancy['currency']}): {vacancy['payment_from']} - {vacancy['payment_to']}.\n"
                      f"Ссылка на вакансию: {vacancy['link']}.\n")

    def top_by_avg_salary(self):
        """
        Метод сортирует вакансии в соответствии с максимальной зарплатой
        """

        leaders_list = []
        with open('sj_Data.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            for vacancy in self.vacancy:
                if vacancy['payment_to'] == 0:
                    continue
                leaders_list.append(vacancy)
        self.sorted_list = sorted(leaders_list, key=lambda data: (data['payment_to']),
                                  reverse=True)[:10]
        for vacancy in self.sorted_list:
            print(f'Название организации: {vacancy["firm_name"]}.\n'
                  f'Наименование вакансии: {vacancy["profession"]}.\n'
                  f'Заработная плата({vacancy["currency"]}): {vacancy["payment_from"]} - {vacancy["payment_to"]}.\n'
                  f'Ссылка на вакансию: {vacancy["link"]}.\n')
