#!/usr/bin/env python3
"""
Cache class that stores instance of Redis client
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Count the number of calls to a method
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Declare a Wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """
    Cache class that stores instance of Redis client
    """
    def __init__(self):
        """
        Cache class that stores instance of Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores input data in Redis using the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Gets the data stored at key and returns it
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Returns a string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Returns an int
        """
        return self.get(key, int)
