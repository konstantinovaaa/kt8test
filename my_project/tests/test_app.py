import pytest
import allure
import asyncio
from my_project.src.app import fetch_json

# Примеры URL для тестирования
URL_1 = "https://jsonplaceholder.typicode.com/todos/1"
URL_404 = "https://jsonplaceholder.typicode.com/nonexistent"

# Фикстура для создания event_loop
@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

# Тест существующего URL
@allure.feature("HTTP Requests")
@allure.story("Fetch JSON from a valid URL")
@pytest.mark.asyncio
async def test_fetch_json_valid_url(event_loop):
    with allure.step("Fetching JSON from a valid URL"):
        json_response = await fetch_json(URL_1)

    assert "userId" in json_response
    assert "id" in json_response
    assert "title" in json_response
    assert "completed" in json_response

# Тест несуществующего URL
@allure.feature("HTTP Requests")
@allure.story("Fetch JSON from a non-existent URL")
@pytest.mark.asyncio
async def test_fetch_json_nonexistent_url(event_loop):
    with allure.step("Fetching JSON from a non-existent URL"):
        with pytest.raises(Exception) as exc_info:
            await fetch_json(URL_404)

        assert "404" in str(exc_info.value)

# Тест с неправильным URL форматом
@allure.feature("HTTP Requests")
@allure.story("Fetch JSON with an invalid URL format")
@pytest.mark.asyncio
async def test_fetch_json_invalid_url(event_loop):
    invalid_url = "invalid_url"
    with allure.step("Fetching JSON with an invalid URL format"):
        with pytest.raises(Exception) as exc_info:
            await fetch_json(invalid_url)

        assert "Invalid URL" in str(exc_info.value)
