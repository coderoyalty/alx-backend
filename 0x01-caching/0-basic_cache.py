#!/usr/bin/env python3
"""
basic cache
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class BasicCache(BaseCaching):
    def __init__(self, *args, **kwargs):
        """
        initialize
        """
        super().__init__(*args, **kwargs)

    def put(self, key, item):
        """
        place an item in the cache dict using its
        key as index
        """
        self.cache_data[key] = item

    def get(self, key):
        """
        fetch an item from the cache
        """
        return self.cache_data.get(key, None)
