from unittest.mock import Mock, patch

import pytest

from src.parser import HeadHunterAPI


class TestHeadHunterAPI:
    """Тесты для класса HeadHunterAPI"""

    @pytest.fixture
    def hh_api(self):
        """Фикстура для создания экземпляра HeadHunterAPI"""
        return HeadHunterAPI()

    @pytest.fixture
    def mock_vacancy_data(self):
        """Фикстура для создания mock данных вакансии"""
        return {
            "name": "Python Developer",
            "id": "12345",
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "snippet": {"requirement": "Experience with Django and Flask"},
        }

    @pytest.fixture
    def mock_response_data(self):
        """Фикстура для создания mock ответа API"""
        return {
            "items": [
                {
                    "name": "Python Developer",
                    "id": "12345",
                    "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
                    "snippet": {"requirement": "Experience with Django and Flask"},
                },
                {
                    "name": "Data Scientist",
                    "id": "67890",
                    "salary": None,
                    "snippet": {"requirement": "Machine learning experience"},
                },
            ]
        }

    @patch("src.parser.requests.get")
    def test_connect_success(self, mock_get, hh_api):
        """Тест успешного подключения"""
        # Настраиваем mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Вызываем метод
        result = hh_api.connect()

        # Проверяем вызовы
        mock_get.assert_called_once_with("https://api.hh.ru/vacancies")
        assert result == 200

    @patch("src.parser.requests.get")
    def test_connect_failure(self, mock_get, hh_api):
        """Тест неуспешного подключения"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = hh_api.connect()

        mock_get.assert_called_once_with("https://api.hh.ru/vacancies")
        assert result == 404

    @patch("src.parser.requests.get")
    def test_get_vacancies_success(self, mock_get, hh_api, mock_response_data, mock_vacancy_data):
        """Тест успешного получения вакансий"""
        # Настраиваем моки
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data

        mock_get.return_value = mock_response

        # Вызываем метод
        result = hh_api.get_vacancies("python")
        print(len(result))

        # Проверяем результат
        assert result[0]["name"] == "Python Developer"
        assert result[0]["vacancy_id"] == "12345"
        assert result[0]["salary"] == {"from": 100000, "to": 150000, "currency": "RUR"}
        assert result[0]["description"] == "Experience with Django and Flask"

        # Проверяем обработку None salary
        assert result[1]["salary"] is None

    @patch("src.parser.requests.get")
    def test_get_vacancies_api_unavailable(self, mock_get, hh_api, capsys):
        """Тест поведения при недоступном API"""
        mock_response = Mock()
        mock_response.status_code = 503
        mock_get.return_value = mock_response

        result = hh_api.get_vacancies("python")

        # Проверяем, что возвращается пустой список
        assert result == []

        # Проверяем вывод сообщения
        captured = capsys.readouterr()
        assert "API не доступен" in captured.out
