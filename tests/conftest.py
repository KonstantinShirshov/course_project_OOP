import pytest

from src.parser import HeadHunterAPI

@pytest.fixture
def headhunter_api():
    api = HeadHunterAPI()  # Создаём экземпляр
    api.params = {"page": 0}  # Переопределяем params, если нужно
    return api