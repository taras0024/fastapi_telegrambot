import functools
import json
import os

from .settings import PAGE_COUNT


def set_env_ngrok_url():
    os.system('curl http://ngrok:4040/api/tunnels > tunnels.json')
    with open('tunnels.json') as file:
        data = json.load(file)

    os.environ['NGROK_URL'] = data['tunnels'][0]['public_url']
    return data['tunnels'][0]['public_url']


def paginate(iterable, _previous=0, _next=0):
    _count = len(iterable) if iterable else 0
    _page = _previous + _next
    MAX_PAGE = _count % PAGE_COUNT and _count // PAGE_COUNT + _count % PAGE_COUNT or _count // PAGE_COUNT

    result = iterable and iterable[_page * PAGE_COUNT:_page * PAGE_COUNT + PAGE_COUNT]
    if not result or _page < 0 or _page >= MAX_PAGE:
        return None, None

    return result, _page


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
