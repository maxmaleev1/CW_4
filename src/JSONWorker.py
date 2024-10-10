import json
import os.path
from abc import ABC, abstractmethod
from config import DATA_PATH


class BaseJSONSaver(ABC):
    # @abstractmethod
    # def add_vacancy(self, vacancy):
    #     pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        '''Заглушка для удаления вакансии из файла'''
        pass

    @abstractmethod
    def filter_vacancies(self, filter_city):
        """Фильтрует список вакансий по городу"""
        pass

class JSONWorker(BaseJSONSaver):
    def __init__(self, file_name__='hh_vacancies.json'):
        self.file_path = os.path.join(DATA_PATH, file_name__)
        self.prepare()

    def prepare(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    # def add_vacancy(self, vacancy):
    #     """Принимает вакансию, преобразует ее в словарь и дописывает в имеющийся файл ('hh_vacancies.json')"""
    #     json.dump([vacancy], 'hh_vacancies.json')

    def add_vacancies(self, hh_vacancies):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            json.dump([hh_vacancies], f, ensure_ascii=False, indent=2)

    @staticmethod
    def filter_vacancies(filter_city, file_name__='hh_vacancies.json'):
        """Фильтрует список вакансий по городу"""
    user_list = []
    with open('file_name__', 'r', encoding='utf=8') as f:
        text = json.load(f)
    for i in text:
        if filter_city in i['area']['name']:
            user_list.append(i)
    # for vacs in user_list:
    #     for k, v in vacs.items():
    #         print(f'{k}:{v}')
        return user_list

    # @staticmethod
    # def sort_by_salary(n, file):
    #     with open(file, 'r', encoding='utf=8') as f:
    #         text = json.load(f)
    #         sorted_list = sorted(text, key=lambda x: x['Зарплата'], reverse=True)
    #         for i in sorted_list[0:n]:
    #             for k, v in i.items():
    #                 print(f'{k}:{v}')
    #             print()


    def del_vacancy(self, vacancy):
        '''Заглушка для удаления вакансии из файла'''
        pass

