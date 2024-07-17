#!/usr/bin/env python3
"""
Cache class that stores instance of Redis client
"""

import redis
import uuid
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores input data in Redis using the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
