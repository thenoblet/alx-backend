#!/usr/bin/python3

"""
LFU Cache Module

This module provides an LFU (Least Frequently Used) caching class that
extends the BaseCaching class.
The LFUCache class implements a caching strategy where the
least frequently accessed items are discarded first when the cache reaches its
maximum capacity. It also incorporates an LRU (Least Recently Used) policy as a
secondary mechanism when multiple items have the same frequency.

Classes:
    - LFUCache: Implements LFU caching strategy with methods to put and
    get items.
"""

from typing import Any, Union
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache: A cache that implements the LFU (Least Frequently Used)
    eviction policy.

    Inherits from BaseCaching and overrides the put and get methods to
    implement LFU caching. If multiple items have the same frequency, it uses
    the LRU (Least Recently Used) policy as a tie-breaker.

    Attributes:
        cache_data (OrderedDict): Stores the cache data with keys and values.
        freq_map (dict): Maps keys to their access frequency.
        order_map (dict): Maps frequencies to OrderedDicts of keys, tracking
                          the order of access within each frequency.
    """
    def __init__(self):
        """
        Initializes the LFUCache instance.

        Sets up the cache with an empty OrderedDict for cache data,
        an empty dictionary for frequency mapping, and an empty dictionary
        for order mapping.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq_map = {}
        self.order_map = {}

    def _update_freq(self, key: Any) -> None:
        """
        Updates the frequency of a key in the cache.

        This method increments the access frequency of the given key
        and moves it to the appropriate position in the order map.

        Args:
            key: The key whose frequency is to be updated.
        """
        if key in self.cache_data:
            freq = self.freq_map.get(key, 0)
            self.freq_map[key] = freq + 1

            if freq in self.order_map:
                del self.order_map[freq][key]
                if not self.order_map[freq]:
                    del self.order_map[freq]

            new_freq = freq + 1
            if new_freq not in self.order_map:
                self.order_map[new_freq] = OrderedDict()
            self.order_map[new_freq][key] = None

    def put(self, key: Any, item: Any) -> None:
        """
        Adds an item to the cache using LFU policy.

        If the key already exists in the cache, it updates the item and
        increases its frequency. If the key does not exist and the cache is
        full, it discards the least frequently used item (and least recently
        used item within that frequency).

        Args:
            key: The key under which the item should be stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_freq(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.order_map.keys())
                lfu_items = self.order_map[min_freq]

                if lfu_items:
                    lru_key, _ = lfu_items.popitem(last=False)
                    print(f"DISCARD: {lru_key}")
                    del self.cache_data[lru_key]
                    del self.freq_map[lru_key]

                if not self.order_map[min_freq]:
                    del self.order_map[min_freq]

            self.cache_data[key] = item
            self.freq_map[key] = 1
            if 1 not in self.order_map:
                self.order_map[1] = OrderedDict()
            self.order_map[1][key] = None

    def get(self, key: Any) -> Union[Any, None]:
        """
        Retrieves an item from the cache.

        If the key exists in the cache, it updates the frequency of the key
        and returns the associated item.
        If the key does not exist, it returns None.

        Args:
            key: The key corresponding to the item to be retrieved.

        Returns:
            The item stored under the key, or None if the key is invalid.
        """
        if key in self.cache_data:
            self._update_freq(key)
            return self.cache_data[key]

        return None
