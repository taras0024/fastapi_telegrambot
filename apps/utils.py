import functools
import json
import os

import aiohttp

from .settings import APP_URL


def set_env_ngrok_url():
    os.system('curl http://ngrok:4040/api/tunnels > tunnels.json')
    with open('tunnels.json') as file:
        data = json.load(file)

    os.environ['NGROK_URL'] = data['tunnels'][0]['public_url']
    return data['tunnels'][0]['public_url']


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
                url=APP_URL,
                headers={},
                json=data
        ) as resp:
            print(await resp.json())

    async def _get_files(self, *args, **kwargs):
        async with self.session.get(
                url=f'{APP_URL}',
        ) as resp:
            json_response = await resp.json()
            return json_response

    async def _get_file(self, params, *args, **kwargs):
        async with self.session.get(
                url=f'{APP_URL}/{params["name"]}'
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


def exception_handler():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                print(e)

        return wrapped

    return wrapper
