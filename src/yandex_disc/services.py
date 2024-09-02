import aiohttp


async def fetch_files_info(public_key):
    url = f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data.get('_embedded'):
                    return [item['name'] for item in data.get('_embedded', {}).get('items', [])]
                elif data.get('type'):
                    return [data['name']]
            else:
                return []
