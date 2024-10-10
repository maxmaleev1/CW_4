def filter_vacancies(vacancies, ключевые_слова):
    return [вакансия for вакансия in vacancies if
            any(ключ.lower() in вакансия['description'].lower() for ключ in ключевые_слова)]



def sort_vacancies(vacancies):
    """
    Сортирует список вакансий по убыванию зарплаты.
    """
    return sorted(vacancies, key=lambda vacancy: vacancy.get('salary_from', 0), reverse=True)



def get_top_vacancies(vacancies, upper_part):
    """
    Возвращает верхнюю часть списка вакансий в соответствии с указанным лимитом.
    """
    return vacancies[:upper_part]

def print_vacancies(vacancies):
    """
    Выводит информацию о вакансиях в консоль.
    """
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            print()
    else:
        print("Нет подходящих вакансий")

# salary_to
# salary_from
# result = sorted(instances_vacancy)