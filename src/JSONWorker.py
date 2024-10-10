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

    def filter_vacancies(self, filter_city):
        """Фильтрует список вакансий по городу"""

        return



    def del_vacancy(self, vacancy):
        pass

