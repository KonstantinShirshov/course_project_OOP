import pytest

from src.saver import JSONSaver


@pytest.fixture
def data_test():
    return [
        {
            "name": "Backend-разработчик",
            "vacancy_id": "124605293",
            "salary": 1000000,
            "description": "Опыт работы с серверной частью (PHP/Laravel, Node.js "
                           "или <highlighttext>Python</highlighttext>/Django/Flask). "
                           "Работа с базами данных (MySQL/PostgreSQL). ",
        }
    ]


def test_write_file(data_test):
    json_saver = JSONSaver("test1.json")
    json_saver.write_file(data_test)
    assert json_saver.read_file() == data_test


def test_add_vacancy(vacancy1):
    json_saver = JSONSaver("test2.json")
    json_saver.add_vacancy(vacancy1)
    assert json_saver.read_file() == [
        {
            "name": "Junior Python Developer",
            "vacancy_id": "105338726",
            "salary": 50000,
            "description": "Требования: опыт работы от 2 лет...",
        }
    ]


def test_delete_vacancy(vacancy1):
    json_saver = JSONSaver("test2.json")
    json_saver.delete_vacancy(vacancy1)
    assert json_saver.read_file() == []
