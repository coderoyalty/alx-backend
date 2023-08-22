#!/usr/bin/env python3
"""
fifo cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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
            """
            :( what was i thinking here
            could have just done!
            keys = list(self.cache_data.keys())
            first_item = keys[0]

            (in kabmy lame's expression)
            """
            keys_iter = iter(self.cache_data.keys())
            first_item = next(keys_iter)
            self.cache_data.pop(first_item)
            print(f"DISCARD {first_item}")
        self.cache_data[key] = item

    def get(self, key):
        """
        get an item from the cache
        """
        return self.cache_data.get(key, None)
