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
    items_count = len(iterable) if iterable else 0
    current_page = _previous + _next
    max_page = items_count % PAGE_COUNT and items_count // PAGE_COUNT + items_count % PAGE_COUNT or items_count // PAGE_COUNT

    result = iterable and iterable[current_page * PAGE_COUNT:current_page * PAGE_COUNT + PAGE_COUNT]
    if not result or current_page < 0 or current_page >= max_page:
        return None, current_page

    return result, current_page


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
