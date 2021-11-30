#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker Module
"""
from typing import Callable
import redis
from functools import wraps
import requests
from datetime import timedelta


cache = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator that count number of requests"""
    @wraps(method)
    def wrapper(*args, **kwds):
        cache.incr("count:{}".format(args[0]), 1)
        return method(*args, **kwds)
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL and returns it."""
    if not cache.exists(url):
        res = requests.get(url)
        cache.setex(url, timedelta(seconds=10), res.content)
        return res.content
    return cache.get(url)
