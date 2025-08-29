

from typing import List, Dict
from abc import ABC, abstractmethod

import requests

from src.vacancy import Vacancy


class Parser(ABC):
    """Абстрактный класс для взаимодействия с API приложениями с вакансиями"""

    @abstractmethod
    def connect(self) -> List:
        """Подключение"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword) -> List:
        """Получение вакансий"""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с Api HeadHunter"""

    def __init__(self):
        """Инициализация"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def connect(self):
        return requests.get(self.__url).status_code


    def get_vacancies(self, keyword) -> List[Dict]:
        vacancies = self.__load_vacancy(keyword)
        vacancy_list = []
        for vacancy in vacancies:
            dct = {"name": vacancy.get('name'),
                   "vacancy_id": vacancy.get('id'),
                   "salary": vacancy.get('salary'),
                   "description": vacancy['snippet'].get('requirement')}
            vacancy_list.append(dct)
        return vacancy_list

    def __load_vacancy(self, keyword) -> List[Dict]:
        self.params['text'] = keyword
        if self.connect() == 200:
            while self.params.get('page') != 5:
                try:
                    response = requests.get(self.__url, headers=self.headers, params=self.params)
                    vacancies = response.json()['items']
                    self.vacancies.extend(vacancies)
                    self.params['page'] += 1
                except requests.exceptions.RequestException:
                    print("Возможна проблема с подключением через API к сайту с вакансиями")
            return self.vacancies
        print("API не доступен")

# if __name__ == "__main__":
#     hh_api = HeadHunterAPI()
#     search_query = input("Введите поисковый запрос: ")
#     hh_vacancies = hh_api.get_vacancies(search_query)
#     print(hh_vacancies)