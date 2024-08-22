#!/usr/bin/python3

"""
MRU Cache Module

This module provides an MRU (Most Recently Used) caching class that extends
the BaseCaching class.
The MRUCache class implements a caching strategy where the most recently
used items are discarded when the cache reaches its maximum capacity.
It allows storing and retrieving items using a dictionary, with an
OrderedDict to track the order of access.

Classes:
    - MRUCache: Implements MRU caching strategy with put and get methods.
"""
from typing import Any, Union
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache: A cache that implements an MRU (Most Recently Used)
    eviction policy.

    Inherits from BaseCaching and overrides the put and get methods to
    implement MRU caching. The most recently used item is removed
    when the cache reaches its maximum capacity.

    Attributes:
        cache_data (OrderedDict): An ordered dictionary that tracks the
                                  order of key access for eviction.
    """

    def __init__(self):
        """
        Initializes the LRUCache instance.

        Sets up the cache with an empty OrderedDict to keep track of the
        order of key access.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: Any, item: Any) -> None:
        """
        Adds an item to the cache using MRU policy.

        If the key already exists in the cache, it updates the item and
        marks it as recently used. If the key does not exist and the cache
        is full, it discards the most recently used item.

        Args:
            key: The key under which the item should be stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                recent_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {recent_key}")

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
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]

        return None
