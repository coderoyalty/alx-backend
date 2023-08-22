#!/usr/bin/env python3
"""
lifo cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching Method Implementation
    """

    def __init__(self):
        """
        initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        add an item to the cache using a key
        as its index
        """
        if not key or not item:
            pass
        keys = self.cache_data.keys()
        if len(self.cache_data) == self.MAX_ITEMS and key not in keys:
            keys = self.cache_data.keys()
            keys = list(keys)
            rm_key = keys[-1]
            self.cache_data.pop(rm_key)
            print(f"DISCARD: {rm_key}")
        self.cache_data[key] = item

    def get(self, key):
        """
        get an item from the cache
        """
        return self.cache_data.get(key, None)
