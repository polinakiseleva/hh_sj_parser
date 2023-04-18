from json_saver import JSONSaverHH, JSONSaverSJ
from vacancy import HeadHunterVacancy, SuperJobVacancy


def main():
    while True:
        print('Здравствуйте!\n'
              'Данная программа предназначена для парсинга вакансий с платформ "HeadHunter" и "SuperJob".\n')

        chosen_platform = input('Пожалуйста, выберете один из доступных сервисов.\n'
                                'Для выбора сервиса введите соответствующий ему номер.\n'
                                '1: HeadHunter\n'
                                '2: SuperJob\n'
                                'Введите номер сервиса: ').strip()

        while chosen_platform not in ('1', '2'):
            chosen_platform = input('Пожалуйста, выберите номер сервиса из списка: ').strip()

        if chosen_platform.strip().upper() == '1':
            vacancy = JSONSaverHH()
        else:
            vacancy = JSONSaverSJ()

        profession = input('Введите название вакансии, которую хотите найти: ')
        vacancy.add_vacancy(profession)

        if chosen_platform.strip().upper() == '1':
            print_vacancies = HeadHunterVacancy()
        elif chosen_platform.strip().upper() == '2':
            print_vacancies = SuperJobVacancy()
        print_vacancies.show_all_vacancies()

        while True:
            answer = input(f"Для отображения дополнительной информации выберите команду из списка:\n"
                           f"1: Просмотр самых высокооплачиваемых вакансий\n"
                           f"2: Выбор другой платформы для поиска вакансий\n"
                           f"3: Завершение программы\n"
                           f"\nПожалуйста, введите номер команды из списка: ").strip()
            while answer not in ('1', '2', '3'):
                answer = input('Пожалуйста, введите номер команды из представленных в списке: ').strip()

            if answer == '1':
                print_vacancies.top_by_avg_salary()
            elif answer == "2":
                print('Перенаправление на выбор другой платформы для поиска вакансий...')
                break
            else:
                exit('Спасибо за использование программы! Работа успешно завершена!\n'
                     'Файл с “сырыми“ данными о собранных вакансиях находится в основной директории\n'
                     'До новых встреч!')


if __name__ == "__main__":
    main()
