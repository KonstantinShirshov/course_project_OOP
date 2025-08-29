from typing import List, Dict


def filter_vacancies(vacancies_list: List, filter_word: str) -> List:
    """Функция для фильтрации вакансий по заданному слову в описании"""

    filter_word = filter_word.lower()
    filtered_vacancies_list = [vacancy for vacancy in vacancies_list if filter_word in vacancy.description.lower()]
    return filtered_vacancies_list


def get_vacancy_by_salary(vacancies_list: List, filter_salary: str) -> List[Dict]:
    """Функция для фильтрации вакансий по заданной зарплате
    (оставляет вакансии с зарплатой выше либо равной указанной пользователем)"""

    filtered_vacancies_list = []
    for vacancy in vacancies_list:
        if vacancy.salary >= int(filter_salary):
            filtered_vacancies_list.append(vacancy)
    return filtered_vacancies_list


def sort_vacancies(vacancies_list: List) -> List:
    """Функция для сортировки вакансий по зарплате (по убыванию)"""

    vacancies_list.sort(key=lambda x: x.salary, reverse=True)
    return vacancies_list


def get_top_vacancies(vacancies_list: List, top_n: int) -> List:
    """Функция для получения топ N вакансий (N указывает пользователь)"""
    top_vacancies = []
    if top_n < len(vacancies_list):
        top_vacancies = vacancies_list[0:(top_n-1)]
        return top_vacancies
    else:
        top_vacancies = vacancies_list
        return top_vacancies


def print_vacancies(vacancies_list: List) -> None:
    """Функция для вывода вакансий на экран"""

    for vacancy in vacancies_list:
        print(f'Вакансия 1: {vacancy}')
    return