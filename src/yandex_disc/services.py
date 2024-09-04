import aiohttp
import requests


async def fetch_files_info(public_key):
    url = f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data.get('_embedded'):
                    return [item for item in data.get('_embedded', {}).get('items', [])]
                elif data.get('type'):
                    return [data]
            else:
                return []


def download_file(public_key):
    url = f'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={public_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        link_for_download = data.get('href')
        return link_for_download
    else:
        print(f"Error fetching download link: {response.status_code}")
        return None
