#!/usr/bin/env python3
"""
Redis basic.
"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class to handle redis operations."""
    def __init__(self):
        """stores an instance of the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes and stores a data argument and returns a string."""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
