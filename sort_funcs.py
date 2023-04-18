def sort_by_max_salary_hh(vacancy):
    """
    Функция сортирует вакансии с hh по максимальной зарплате
    """
    return sorted(vacancy, key=lambda data: (data["salary"]["to"] is None, data["salary"]["to"]),
                  reverse=True)


def sort_by_max_salary_sj(vacancy):
    """
    Функция сортирует вакансии с sj по максимальной зарплате
    """
    return sorted(vacancy, key=lambda data: (data['payment_to'] == 0, data['payment_to']),
                  reverse=True)
