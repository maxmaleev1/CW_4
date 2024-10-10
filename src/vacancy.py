class Vacancy:
    __slots__ = ('title', 'alternate_url', 'name', 'salary')
    def __init__(self, title, alternate_url, name, salary):
        self.title = title
        self.alternate_url = alternate_url
        self.name = name
        self.salary = salary
        self.validate__()

    def validate__(self):
        if not self.salary:
            self.salary_from = 0
            self.salary_to = 0
            return

        if not self.salary["from"]:
            self.salary_from = 0
        else:
            self.salary_from = self.salary["from"]

        if not self.salary["to"]:
            self.salary_to = 0
        else:
            self.salary_to = self.salary["to"]


    @classmethod
    def create_vacancies(cls, hh_vacancies):
        instances_vacancy = []
        for vacancies_info in hh_vacancies:
            title = vacancies_info['name']
            alternate_url = vacancies_info['alternate_url']
            salary = vacancies_info['salary']
            name = vacancies_info['area']['name']
            vacancy = cls(title, alternate_url, name, salary)
            instances_vacancy.append(vacancy)
        return instances_vacancy


    def __lt__(self, other):
        if self.salary_from:
            if self.salary_from < other.salary_from:
                return True
            else:
                return False
        else:
            if other.salary_from:
                return False

    def __str__(self):
        return f'{self.title}: ЗП от {self.salary_from} до {self.salary_to}- {self.alternate_url}'