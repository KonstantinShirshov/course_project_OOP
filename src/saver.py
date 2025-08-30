import json
import os
from abc import ABC, abstractmethod
from typing import List, Dict

from src.vacancy import Vacancy


class Saver(ABC):
    """Абстрактный класс для сохранения данных с вакансиями в файл разном виде"""

    @abstractmethod
    def read_file(self):
        """Функция для получения вакансий из файла"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Функция для добавления вакансии"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Функция для удаления вакансий"""
        pass

class JSONSaver(Saver):
    """Класс для сохранения данных в файл JSON и работы с ним"""

    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = self.get_data_file_path(filename)
        self.ensure_file_exists()

    @staticmethod
    def get_data_file_path(filename: str) -> str:
        """Возвращает полный путь к файлу в папке data"""
        # Получаем путь к текущей директории (где находится скрипт)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Поднимаемся на уровень выше (из src в корневую директорию)
        root_dir = os.path.dirname(current_dir)

        # Создаем путь к папке data
        data_dir = os.path.join(root_dir, "data")

        # Создаем папку data, если она не существует
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Возвращаем полный путь к файлу
        return os.path.join(data_dir, filename)

    @property
    def filename(self) -> str:
        """Получение имени файла"""
        return self.__filename

    def ensure_file_exists(self) -> None:
        """Создает файл, если он не существует"""
        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def read_file(self) -> List[Dict]:
        """Метод, который читает данные из файла"""
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def write_file(self, data: List[Dict]) -> None:
        """Метод, который записывает данные в файл"""
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, new_vacancy: Vacancy) -> None:
        """Метод, добавляющий и записывающий вакансию в файл"""
        vacancies = self.read_file()
        new_vacancy_id = new_vacancy.to_dict().get('vacancy_id')

        vacancy_exist = False
        for vacancy in vacancies:
            if new_vacancy_id == vacancy.get('vacancy_id'):
                vacancy_exist = True
                break
        if not vacancy_exist:
            vacancies.append((new_vacancy.to_dict()))
            self.write_file(vacancies)
        else:
            print("Нет новых вакансий для добавления")

    def delete_vacancy(self, vacancy_for_delete: Vacancy) -> None:
        """Метод для удаления вакансии из файла и сохранения оставшихся вакансий в файл"""
        vacancies = self.read_file()
        vacancy_to_delete_id = vacancy_for_delete.to_dict().get('vacancy_id')

        # Ищем вакансию для удаления
        vacancy_to_remove = None
        for vacancy in vacancies:
            if vacancy_to_delete_id == vacancy.get('vacancy_id'):
                vacancy_to_remove = vacancy
                break

        # Если вакансия найдена, удаляем её
        if vacancy_to_remove:
            vacancies.remove(vacancy_to_remove)
            self.write_file(vacancies)
        else:
            print("Файл не содержит удаляемую вакансию")
