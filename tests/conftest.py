import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy1() -> Vacancy:
    return Vacancy("Junior Python Developer",
        "105338726",
        {"from": 50000},
        "Требования: опыт работы от 2 лет...")


@pytest.fixture
def vacancy2() -> Vacancy:
    return Vacancy("Junior Python Developer",
         "105338543",
         {"to": 150000},
         "Требования: опыт работы от 1 года...")

@pytest.fixture
def vacancy3() -> Vacancy:
    return Vacancy("Go Developer",
            "105354667",
            {"from": 80000, "to": 140000},
            "Требования: опыт работы от 3 лет...")

@pytest.fixture
def vacancy4() -> Vacancy:
    return Vacancy("Java Developer",
            "10456933",
            None,
            "Опыт работы с языками программирования (например: <highlighttext>Python</highlighttext>, JavaScript, Java)")

@pytest.fixture
def vacancies_list_1(vacancy1, vacancy2, vacancy3):
    return [vacancy1, vacancy2, vacancy3]

@pytest.fixture
def vacancies_list_dicts():
    return [{"name": "Junior Python Developer",
             "vacancy_id": "105338726",
             "salary": 50000,
             "description": "Требования: опыт работы от 2 лет..."},
            {"name": "Junior Python Developer",
             "vacancy_id": "105338543",
             "salary": 150000,
             "description": "Требования: опыт работы от 1 года..."},
            {"name": "Go Developer",
             "vacancy_id": "105354667",
             "salary": 140000,
             "description": "Требования: опыт работы от 3 лет..."}]