#!/usr/bin/env python3
"""
Exercise Module
"""
from typing import Callable, Union
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that count number of calls"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(method.__qualname__, 1)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator to store the history of inputs and outputs for a
    particular function"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        in_list_name = "{}:inputs".format(method.__qualname__)
        out_list_name = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(in_list_name, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(out_list_name, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """Method that display the history of calls of a particular
    function."""
    redis_ins = redis.Redis()
    fn_name = method.__qualname__
    inputs = redis_ins.lrange("{}:inputs".format(fn_name), 0, -1)
    outputs = redis_ins.lrange("{}:outputs".format(fn_name), 0, -1)

    try:
        count = redis_ins.get(fn_name).decode('utf-8')
    except Exception:
        count = 0

    print("{} was called {} times:".format(fn_name, count))
    for key, value in zip(outputs, inputs):
        print("{}(*{}) -> {}".format(fn_name,
              value.decode('utf-8'), key.decode('utf-8')))


class Cache:
    """
    Cache class
    """

    def __init__(self) -> None:
        """Instantiation"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that takes a data argument and returns a string key"""
        ran_key = str(uuid.uuid4())
        self._redis.set(ran_key, data)
        return ran_key

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes,
                                                          int,
                                                          float]:
        """Method that take a key string argument and an optional Callable
        and return a value with desiret format"""
        if not fn:
            value = self._redis.get(key)
            return value
        value = fn(self._redis.get(key))
        return value

    def get_str(self, key: str) -> str:
        """Method that take a key string argument and return a value as str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Method that take a key string argument and return a value as int"""
        return self.get(key, int)
