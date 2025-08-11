import pytest
from unittest.mock import patch, Mock
from typing import List, Dict

import requests

from src.parser import HeadHunterAPI

@pytest.fixture
def headhunter_api():
    api = HeadHunterAPI()  # Создаём экземпляр
    api.params = {"page": 0}  # Переопределяем params, если нужно
    return api

@patch("src.parser.requests.get")
def test_get_vacancies(mock_get, headhunter_api):
    # Настраиваем мок
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"id": 1, "name": "Python Dev"}]}
    mock_get.return_value = mock_response

    # Вызываем метод
    result = headhunter_api.get_vacancies("Python")

    # Проверяем
    assert len(result) > 0
    assert result[0]["id"] == 1
    assert headhunter_api.params["page"] > 0

@patch("src.parser.HeadHunterAPI.connect")  # Мокаем метод connect
def test_api_unavailable_message(mock_connect, headhunter_api, capsys):
    # Настраиваем мок, чтобы connect() вернул код != 200
    mock_connect.return_value = 404

    # Вызываем метод, который должен вывести сообщение
    result = headhunter_api.get_vacancies("Python")

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем:
    assert result is None  # Метод вернул None
    assert "API не доступен" in captured.out



