#!/usr/bin/env python3
"""
Implements an expiring web cache and tracker
"""
from typing import Callable
from functools import wraps
import redis
import requests
redis_client = redis.Redis()
count = 0


def url_count(method: Callable) -> Callable:
    """decorator for url count"""
    @wraps(method)
    def wrapper(*args):
        redis_client.incr(f"count:{args[0]}")
        return method(*args)
    return wrapper


@url_count
def get_page(url: str) -> str:
    """ get a page and cache value"""
    redis_client.set(f'cached:{url}', count)
    response = requests.get(url)
    redis_client.setex(f'cached:{url}', 10, redis_client.get(f'cached:{url}'))
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
