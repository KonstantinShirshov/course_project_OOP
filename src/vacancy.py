

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
        """Валидация и нормализация зарплаты"""
        if isinstance(salary, dict):
            # Если salary - словарь (как приходит из API)
            if salary.get('to'):
                return salary.get('to')
            elif salary.get('from'):
                return salary.get('from')
            else:
                return 0
        elif isinstance(salary, (int, float)):
            # Если salary - число (как вы передаете в примере)
            return salary
        else:
            return 0

    def to_dict(self):
        """Создание словаря вакансий"""
        return {'name': self.name, 'vacancy_id': self.vacancy_id, 'salary': self.salary, 'description': self.description}

    @staticmethod
    def objects_to_dicts(vacancy_objects):
        return [vacancy.to_dict() for vacancy in vacancy_objects]

    @staticmethod
    def cast_to_object_list(vacancies_list):
        vacancy_objects = []
        for vacancy in vacancies_list:
            vacancy_objects.append(Vacancy(vacancy.get('name'), vacancy.get('vacancy_id'), vacancy.get('salary'), vacancy.get('description')))
        return vacancy_objects


if __name__ == "__main__":
    vac1 = Vacancy("Developer", "1021", 100000, "Опыт работы от 2 лет...")
    print(vac1.salary)