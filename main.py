from src.api import HHAPI
from src.JSONWorker import JSONWorker
from src.utils import print_vacancies, sort_vacancies, get_top_vacancies, filter_vacancies


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    keyword_user = input('Введите фильтр для поиска вакансий: ').capitalize()
    filter_city = input("Введите город: ").capitalize()
    top_n = int(input("Введите количество вакансий для вывода в топ по зп: "))
    print('-' * 100)
    # ПОЛУЧАЕМ ВАКАНСИИ С API И ЗАПИСЫВАЕМ В 'hh_vacancies.json':
    hh_api = HHAPI()
    json_worker = JSONWorker()
    json_worker.add_vacancies(hh_api.get_vacancies__(keyword_user))
    # ПРЕОБРАЗОВАНИЕ В ЭКЗЕМПЛЯРЫ КЛАССА:
    instances_vacancies = json_worker.read_vacancies()
    filtered_vacancies = filter_vacancies(instances_vacancies, filter_city)
    top_vacancies = get_top_vacancies(filtered_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == '__main__':
    user_interaction()
    print("ВЫПОЛНЕНИЕ ЗАВЕРШЕНО. УДАЧНОГО ТРУДОУСТРОЙСТВА!:)*")

