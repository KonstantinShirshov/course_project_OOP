import pytest

from src.vacancy import Vacancy

def test_init(vacancy1, vacancy2, vacancy3, vacancy4):
    assert vacancy1.name == "Junior Python Developer"
    assert vacancy1.vacancy_id == "105338726"
    assert vacancy1.salary == 50000
    assert vacancy1.description == "Требования: опыт работы от 2 лет..."
    assert vacancy2.name == "Junior Python Developer"
    assert vacancy2.vacancy_id == "105338543"
    assert vacancy2.salary == 150000
    assert vacancy2.description == "Требования: опыт работы от 1 лет..."
    assert vacancy3.salary == 140000
    assert vacancy4.salary == 0

def test_to_dict(vacancy1):
    assert Vacancy.to_dict(vacancy1) == {"name": "Junior Python Developer", "vacancy_id": "105338726", "salary": 50000,
                                         "description": "Требования: опыт работы от 2 лет..."}

def test_objects_to_dicts(vacancies_list_1):
    assert Vacancy.objects_to_dicts(vacancies_list_1)[0] == {"name": "Junior Python Developer", "vacancy_id": "105338726", "salary": 50000,
                                         "description": "Требования: опыт работы от 2 лет..."}
    assert Vacancy.objects_to_dicts(vacancies_list_1)[2] == {"name": "Go Developer",
                                                             "vacancy_id": "105354667", "salary": 140000,
                                                             "description": "Требования: опыт работы от 3 лет..."}

def test_cast_to_objects_list(vacancies_list_dicts):
    assert Vacancy.cast_to_object_list(vacancies_list_dicts) == [Vacancy("Junior Python Developer",
                                                                         "105338726",
                                                                         50000,
                                                                         "Требования: опыт работы от 2 лет..."),
                                                                 Vacancy("Junior Python Developer",
                                                                         "105338543",
                                                                         150000,
                                                                         "Требования: опыт работы от 1 года..."),
                                                                 Vacancy("Go Developer",
                                                                         "105354667",
                                                                         140000,
                                                                         "Требования: опыт работы от 3 лет...")]
