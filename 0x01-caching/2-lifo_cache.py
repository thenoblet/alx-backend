#!/usr/bin/python3

"""
LIFO Cache Module

This module provides a LIFO (Last-In-First-Out) caching class that extends
the BaseCaching class.
The LIFOCache class implements a caching strategy where the most recently
added items are discarded when the cache reaches its maximum capacity.
It allows storing and retrieving items using a dictionary, with an
additional list to track the order of item insertion.

Classes:
    - LIFOCache: Implements LIFO caching strategy with put and get methods.
"""
from typing import Any, Union

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache: A cache that implements a LIFO (Last-In-First-Out)
    eviction policy.

    Inherits from BaseCaching and overrides the put and get methods to
    implement LIFO caching. The most recently added item is removed
    when the cache reaches its maximum capacity.

    Attributes:
        keys (List[Any]): A list that tracks the order of keys for eviction.
    """

    def __init__(self):
        """
        Initializes the LIFOCache instance.

        Sets up the cache with an empty dictionary and an empty list
        to keep track of the order of keys.
        """
        super().__init__()
        self.keys = []

    def put(self, key: Any, item: Any) -> None:
        """
        Adds an item to the cache using LIFO policy.

        If the key already exists in the cache, it updates the item
        and moves the key to the end of the order list. If the key
        does not exist and the cache is full, it discards the most
        recently added item.

        Args:
            key: The key under which the item should be stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.keys.remove(key)
            self.keys.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                recent_key = self.keys.pop()
                del self.cache_data[recent_key]
                print(f"DISCARD: {recent_key}")

            self.keys.append(key)
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
