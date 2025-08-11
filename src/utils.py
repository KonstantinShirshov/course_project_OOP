from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс для сохранения данных с вакансиями в файл разном виде"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Функция для добавления вакансии"""
        pass

    @abstractmethod
    def read_file(self):
        """Функция для получения вакансий из файла"""
        pass

    @abstractmethod
    def delete_vacancies(self):
        """Функция для удаления вакансий"""
        pass

class JSONSaver(Saver):
    """Класс для сохранения данных в файл JSON и работы с ним"""

    def


    def add_vacancy(self, vacancy):
        pass

    def read_file(self):
        pass

    def delete_vacancies(self):
        pass

