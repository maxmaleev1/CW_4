from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies__(self, keyword):
        pass

class HHAPI(BaseAPI):
    def __init__(self):
        self.url__ = 'https://api.hh.ru/vacancies'
        self.params__ = {'text': '', 'page': 0, 'per_page': 100, 'area': 113}

    def get_vacancies__(self, keyword):
        self.params__.update({'text': keyword})
        response = requests.get(self.url__, params=self.params__)
        return response.json()["items"]
        # print(response.json()["items"])


if __name__ == '__main__':
    my_api = HHAPI()
    response = my_api.get_vacancies('крановщик')
    pass