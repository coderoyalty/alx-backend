#!/usr/bin/env python3
"""
least recently used (lru) cache
"""
from base_caching import BaseCaching
import sys


class LRUCache(BaseCaching):
    """
    LRU Cache Method Implementation
    """

    def __init__(self):
        """initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        add an item to the cache using a key
        as its index
        """
        if not key or not item:
            return
        keys = self.cache_data.keys()

        if len(self.cache_data) == self.MAX_ITEMS and key not in keys:
            rm_key = self.order.pop()
            self.cache_data.pop(rm_key)
            print(f"DISCARD: {rm_key}")
        if key in keys:
            self.order.remove(key)
        self.cache_data[key] = item
        self.order.insert(0, key)

    def get(self, key):
        """
        get an item from the cache
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.insert(0, key)

        return self.cache_data.get(key, None)
