#!/usr/bin/python3

"""
FIFO Cache Module

This module provides a FIFO (First-In-First-Out) caching class that extends
the BaseCaching class.
The FIFOCache class implements a basic caching strategy where the oldest
items are discarded when the cache reaches its maximum capacity. It allows
storing and retrieving items using a dictionary, with an additional list to
track the order of item insertion.

Classes:
    - FIFOCache: Implements FIFO caching strategy with put and get methods.
"""
from typing import Any, Union

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache: A cache that implements a FIFO (First-In-First-Out)
    eviction policy.

    Inherits from BaseCaching and overrides the put and get methods to
    implement FIFO caching. The oldest item is removed when the cache
    reaches its maximum capacity.

    Attributes:
        keys (List[Any]): A list that tracks the order of keys for eviction.
    """

    def __init__(self):
        """
        Initializes the FIFOCache instance.

        Sets up the cache with an empty dictionary and an empty list
        to keep track of the order of keys.
        """
        super().__init__()
        self.keys = []

    def put(self, key: Any, item: Any) -> None:
        """
        Adds an item to the cache using FIFO policy.

        If the key already exists in the cache, it updates the item
        and moves the key to the end of the order list. If the key
        does not exist and the cache is full, it discards the oldest
        item.

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
                oldest_key = self.keys.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

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
