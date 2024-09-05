import requests
from cachetools import TTLCache, cached
from requests import Response

cache = TTLCache(maxsize=100, ttl=30)


@cached(cache)
def fetch_files_info(public_key) -> list[dict]:
    """Возвращает информацию о файлах содержащихся по переданному public_key."""
    url: str = f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}'

    response: Response = requests.get(url)
    if response.status_code == 200:
        data: dict = response.json()
        if data.get('_embedded'):
            return [item for item in data.get('_embedded', {}).get('items', [])]
        elif data.get('type'):
            return [data]
    else:
        return []


def download_file(public_key) -> str | None:
    """Скачивает файл или папку по public_key."""
    url = f'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={public_key}'

    response: Response = requests.get(url)
    if response.status_code == 200:
        data: dict = response.json()
        link_for_download = data.get('href')
        return link_for_download
    else:
        print(f"Error fetching download link: {response.status_code}")
        return None
