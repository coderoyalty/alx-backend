#!/usr/bin/env python3
"""
simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple containing a start
    index and an end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        implement pagination on a dataset, and return a page of data.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page > 0
        data = []
        start, end = index_range(page, page_size)
        self.dataset()
        try:
            data = self.__dataset[start:end]
        except Exception:
            pass
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        hypermedia pagination
        """
        data = self.get_data(page, page_size)

