from typing import Dict, List


class Vacancy:
    """Класс для вакансий"""

    name: str
    vacancy_id: str
    salary: int | None
    description: str

    __slots__ = ("name", "vacancy_id", "salary", "description")

    def __init__(self, name, vacancy_id, salary, description) -> None:
        """Инициализация"""
        self.name = name
        self.vacancy_id = vacancy_id
        self.salary = self.__salary_valid(salary)
        self.description = description

    def __lt__(self, other):
        """Магический метод сравнения вакансий"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Магический метод сравнения вакансий"""
        return self.salary > other.salary

    @staticmethod
    def __salary_valid(salary):
        """Валидация и нормализация зарплаты"""
        if isinstance(salary, dict):
            if salary.get("to"):
                return salary.get("to")
            elif salary.get("from"):
                return salary.get("from")
            else:
                return 0
        elif isinstance(salary, (int, float)):
            return salary
        else:
            return 0

    def to_dict(self) -> Dict:
        """Создание словаря из вакансии"""
        return {
            "name": self.name,
            "vacancy_id": self.vacancy_id,
            "salary": self.salary,
            "description": self.description,
        }

    @staticmethod
    def objects_to_dicts(vacancy_objects: List) -> List[Dict]:
        """Создание списка словарей из списка объектов класса Vacancy"""
        return [vacancy.to_dict() for vacancy in vacancy_objects]

    @staticmethod
    def cast_to_object_list(vacancies_list: List[Dict]) -> List:
        """Создание списка объектов класса Vacancy из списка словарей"""
        vacancy_objects = []
        for vacancy in vacancies_list:
            vacancy_objects.append(
                Vacancy(
                    vacancy.get("name"), vacancy.get("vacancy_id"), vacancy.get("salary"), vacancy.get("description")
                )
            )
        return vacancy_objects
