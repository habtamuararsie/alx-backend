#!/usr/bin/env python3
""" Task 0 genrate index range"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int): the current page
        page_size (int): the size of items in a page
        first_index: calculate the first index
        last_index: calculate the last index 
        indexOfrange: return first index and last index 
    Returns:
        (tuple): a row/tuple of the start and end index of the given page
    """
    return ((page - 1) * page_size, page * page_size)
