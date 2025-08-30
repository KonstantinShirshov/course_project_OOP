from src.parser import HeadHunterAPI
from src.saver import JSONSaver
from src.utils import filter_vacancies, get_vacancy_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy


def user_interaction():
    """Функция взаимодействия с пользователем"""

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формат JSON
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    print(hh_vacancies)
    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

        # Пример работы конструктора класса с одной вакансией
    vacancy = Vacancy("Python Developer",
                      "123456",
                      "100000-150000",
                      "Требования опыт работы от 3 лет ..." )


    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.write_file(Vacancy.objects_to_dicts(vacancies_list))
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)

    # filter_word = input("Введите ключевое слово для фильтрации вакансий: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # salary_range = input("Введите минимальную зарплату: ")
    #
    # filtered_vacancies = filter_vacancies(vacancies_list, filter_word)
    #
    # ranged_vacancies = get_vacancy_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # json_saver.write_file(Vacancy.objects_to_dicts(top_vacancies))
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
