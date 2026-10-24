import os

def test_project_structure():
    """Тест проверяет, что все критически важные файлы на месте"""
    assert os.path.exists("orbitr.py") is True
    assert os.path.exists("requirements.txt") is True

def test_dummy_analysis():
    """Тест проверяет базовую логику (пример заглушки)"""
    review = "Отличный сервис, мне очень понравилось!"
    assert len(review) > 0
