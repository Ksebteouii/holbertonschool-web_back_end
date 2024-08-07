#!/usr/bin/env python3
"""1-simple_pagination.py"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        rus = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(rus):
            return []
        return rus[start:end]
