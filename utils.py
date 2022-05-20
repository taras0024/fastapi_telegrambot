import aiohttp

from config import URL


class AsyncContextManager:
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session is not None:
            await self.session.close()

    async def _create_file(self, data, *args, **kwargs):
        async with self.session.post(
                url=URL,
                headers={},
                json=data
        ) as resp:
            print(await resp.json())

    async def _get_files(self, *args, **kwargs):
        async with self.session.get(
                url=f'{URL}',
        ) as resp:
            json_response = await resp.json()
            return json_response

    async def _get_file(self, params, *args, **kwargs):
        async with self.session.get(
                url=f'{URL}/{params["name"]}'
        ) as resp:
            json_response = await resp.json()
            return json_response


async def get_files():
    async with AsyncContextManager() as s:
        return await s._get_files()


async def get_file(params):
    async with AsyncContextManager() as s:
        return await s._get_file(params)


async def create_file(data):
    async with AsyncContextManager() as s:
        return await s._create_file(data)
