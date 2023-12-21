import aiohttp
import asyncio
import json

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Проверяем успешность запроса
            response.raise_for_status()

            # Получаем JSON из ответа
            json_data = await response.json()

    return json_data

async def main():
    # Пример использования: замените URL на нужный
    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        json_response = await fetch_json(url)
        print("JSON Response:", json.dumps(json_response, indent=2))
    except aiohttp.ClientError as e:
        print(f"Error during request: {e}")

# Запускаем асинхронное приложение
if __name__ == "__main__":
    asyncio.run(main())
