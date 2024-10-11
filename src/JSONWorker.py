import json
import os.path
from abc import ABC, abstractmethod
from config import DATA_PATH
from src.vacancy import Vacancy


class BaseJSONSaver(ABC):

    @abstractmethod
    def add_vacancies(self, vacancies):
        """Метод для сохранения API запроса с вакансиями в файл json"""
        pass

    @abstractmethod
    def read_vacancies(self):
        """Метод для чтения вакансий из файла json"""
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        """Заглушка для удаления вакансии из файла"""
        pass

class JSONWorker(BaseJSONSaver):

    def __init__(self, file_name__='hh_vacancies.json'):
        self.file_path = os.path.join(DATA_PATH, file_name__)
        self.prepare()

    def prepare(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def add_vacancies(self, hh_vacancies):
        """Метод для сохранения API запроса с вакансиями в файл json"""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(hh_vacancies, f, ensure_ascii=False, indent=2)

    def read_vacancies(self):
        """Метод для чтения вакансий из файла json"""
        with open(self.file_path, encoding='utf-8') as f:
            vacancies = json.load(f)
        return Vacancy.create_vacancies(vacancies)

    def del_vacancy(self, vacancy):
        """Заглушка для удаления вакансии из файла"""
        pass