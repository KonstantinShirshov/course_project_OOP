from src.utils import filter_vacancies, get_top_vacancies, get_vacancy_by_salary, sort_vacancies


def test_filter_vacancies_by_keyword(vacancies_list_2):
    """Тест фильтрации вакансий по ключевому слову"""

    result = filter_vacancies(vacancies_list_2, "опыт")

    assert len(result) == 3
    assert all("опыт" in vacancy["description"].lower() for vacancy in result)
    assert result[0]["name"] == "Junior Python Developer"
    assert result[1]["name"] == "Go Developer"
    assert result[2]["name"] == "Java Developer"


def test_filter_vacancies_no_matches(vacancies_list_2):
    """Тест фильтрации при отсутствии совпадений"""

    result = filter_vacancies(vacancies_list_2, "навыки")

    assert len(result) == 0


def test_filter_vacancies_empty_list():
    """Тест фильтрации пустого списка"""
    result = filter_vacancies([], "python")

    assert len(result) == 0


def test_get_vacancy_by_salary(vacancies_list_dicts):
    """Тест фильтрации по зарплате"""

    result = get_vacancy_by_salary(vacancies_list_dicts, "90000")

    assert len(result) == 2
    assert all(vacancy.salary >= 90000 for vacancy in result)
    salaries = [vacancy.salary for vacancy in result]
    assert 150000 in salaries
    assert 140000 in salaries


def test_sort_vacancies(vacancies_list_2):
    """Тест сортировки вакансий по зарплате"""

    result = sort_vacancies(vacancies_list_2.copy())

    assert len(result) == 4
    salaries = [vacancy.salary for vacancy in result]
    assert salaries == [150000, 140000, 50000, 0]
    assert result[0].salary == 150000
    assert result[-1].salary == 0


def test_sort_vacancies_empty_list():
    """Тест сортировки пустого списка"""
    result = sort_vacancies([])

    assert len(result) == 0


def test_get_top_vacancies(vacancies_list_2):
    """Тест получения топ N вакансий"""
    sorted_list = sort_vacancies(vacancies_list_2)
    result = get_top_vacancies(sorted_list, 2)

    assert len(result) == 2
    salaries = [vacancy.salary for vacancy in result]
    assert salaries == [150000, 140000]


def test_get_top_vacancies_more_than_available(vacancies_list_2):
    """Тест получения топ N, когда N больше количества вакансий"""

    result = get_top_vacancies(vacancies_list_2, 5)

    assert len(result) == 4
    assert result == vacancies_list_2


def test_get_top_vacancies_zero(vacancies_list_2):
    """Тест получения топ 0 вакансий"""

    result = get_top_vacancies(vacancies_list_2, 0)

    assert len(result) == 0


def test_get_top_vacancies_empty_list():
    """Тест получения топ N из пустого списка"""
    result = get_top_vacancies([], 5)

    assert len(result) == 0
