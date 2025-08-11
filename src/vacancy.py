

class Vacancy:
    """Класс для вакансий"""
    name: str
    vacancy_id: str
    salary: int | None
    description: str

    __slots__ = ('name', 'vacancy_id', 'salary', 'description')

    def __init__(self, name, vacancy_id, salary, description):
        """Инициализация"""
        self.name = name
        self.vacancy_id = vacancy_id
        self.salary = self.__salary_valid(salary)
        self.description = description

    @staticmethod
    def __salary_valid(salary):
        """Валидация"""
        if salary:
            if salary.get('to'):
                return salary.get('to')
            else:
                return salary.get('from')
        else:
            return 0

    def vacancy_dict(self):
        """Создание словаря вакансий"""
        return {'name': self.name, 'vacancy_id': self.vacancy_id, 'salary': self.salary, 'description': self.description}

    def __lt__(self, other):
        """"Магический метод сравнения вакансий"""
        return self.salary < other.salary

    def __le__(self, other):
        """"Магический метод сравнения вакансий"""
        return self.salary <= other.salary

    def __gt__(self, other):
        """Магический метод сравнения вакансий"""
        return self.salary > other.salary

    def __ge__(self, other):
        """"Магический метод сравнения вакансий"""
        return self.salary >= other.salary

