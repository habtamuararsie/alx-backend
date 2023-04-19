#!/usr/bin/env python3
"""[summary]"""
import csv
import math
from typing import List


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


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    Returns:
    (tuple): a row/tuple of the start and end index of the given page
    """

    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    indexOfrange = first_index, last_index
    return indexOfrange


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """
     return the appropriate page of the dataset
    """
    self.__dataset = self.dataset()
    assert type(page) is int and type(page_size) is int
    assert page > 0 and page_size > 0
    index = self.index_range(page, page_size)
    res = self.__dataset[index[0]:index[1]] if index[0] < len(
        self.__dataset) and index[1] < len(self.__dataset) else []
    return res
