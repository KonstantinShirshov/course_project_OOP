from src.parser import HeadHunterAPI


def user_interaction():
    """Функция взаимодействия с пользователем"""

    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_api.load_vacancies(search_query)
    hh_vacancies = hh_api.get_vacancies()

    json_saver = JSONSAver()
