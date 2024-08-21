#!/usr/bin/python3

"""
Basic Cache Module

This module provides a basic caching class that extends the BaseCaching
class. The BasicCache class implements a simple key-value store without
any advanced caching strategies. It allows storing and retrieving items
using a dictionary, where items are identified by unique keys.

Classes:
    - BasicCache: Implements basic put and get methods for caching.
"""
from typing import Any, Union

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache: A basic cache that stores key-value pairs.

    Inherits from the BaseCaching class and provides basic implementations
    of the put and get methods without any eviction policy.
    """
    def put(self, key: Any, item: Any) -> None:
        """
        Adds an item to the cache.

        If either the key or item is None, the method does nothing.

        Args:
            key: The key under which the item should be stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key: Any) -> Union[Any, None]:
        """
        Retrieves an item from the cache.

        If the key is None or does not exist in the cache,
        the method returns None.

        Args:
            key: The key corresponding to the item to be retrieved.

        Returns:
            The item stored under the key, or None if the key is invalid.
        """
        if key is None:
            return None

        return self.cache_data.get(key)
