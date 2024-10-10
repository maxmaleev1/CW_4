from src.api import HHAPI
from src.vacancy import Vacancy
from src.JSONWorker import JSONWorker
from src.utils import print_vacancies, sort_vacancies, get_top_vacancies


def user_interaction():
    # keyword_user = input('Введите фильтр для поиска вакансий: ')
    keyword_user = 'инженер'
    # filter_city = input("Введите город: ").capitalize()
    # filtered_vacancies = filter_city(vacancies_list, filter_words)
    # # top_n = int(input("Введите количество вакансий для вывода в топ по зп: "))
    # top_n = 100

    # ПОЛУЧАЕМ ВАКАНСИИ С API И ЗАПИСЫВАЕМ В 'hh_vacancies.json':
    JSONWorker.add_vacancies(HHAPI.get_vacancies__(keyword_user))


    # json_worker = JSONWorker('hh_vacancies.json')
    # Преобразование набора данных из JSON в список объектов:
    # instances_vacancy = Vacancy.create_vacancies(hh_vacancies)
    # print(instances_vacancy)
    # vacancies_list = JSONWorker.add_vacancies(instances_vacancy)
    # print(vacancies_list)
    # if hh_vacancies:
    #     vacancies_list = []
    #     for v in hh_vacancies:
    #         vacancies_list.append(v)
    #     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #     sorted_vacancies = sort_vacancies(filtered_vacancies)
    #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #     print_vacancies(top_vacancies)
    # else:
    #     print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")


if __name__ == '__main__':
    user_interaction()
    print("Выполнение завершено.")

    #
    # sorted_vacancies = sort_vacancies(filtered_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)
    # hh_vacancies = hh_api.get_vacancies(keyword_user)
    # """ПОЛУЧАЕМ СПИСОК СЛОВАРЕЙ С ВАКАНСИЯМИ. ЭТО НЕ ФАЙЛ"""
    # json_worker = JSONWorker('hh_vacancies.json')
    #
