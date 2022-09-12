import aiohttp

from ..settings import APP_URL


class AsyncContextManager:
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session is not None:
            self.session = await self.session.close()

    async def create_file(self, data):
        async with self.session.post(url=APP_URL, headers={}, json=data) as resp:
            print(await resp.json())

    async def get_files(self):
        async with self.session.get(url=f'{APP_URL}') as resp:
            json_response = await resp.json()
            return json_response

    async def get_file(self, params):
        async with self.session.get(url=f'{APP_URL}/{params["name"]}') as resp:
            json_response = await resp.json()
            return json_response
