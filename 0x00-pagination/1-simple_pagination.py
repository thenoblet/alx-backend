#!/usr/bin/env python3

"""
This module implements a simple pagination class.
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    @staticmethod
    def index_range(
        page: int,
        page_size: int
    ) -> Tuple[int, int]:
        """
        Returns a tuple of size two containing a start index and an end index

        Args:
            page (int): The current page number (1-indexed)
            page_size (int): The number of items per page

        Returns:
            Tuple[int, int]: A tuple containing the start and end index
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the page with the given page number and page size.

        Args:
            page (int, optional): The current page number (1-indexed).
            Defaults to 1.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            List[List]: The page with the given page number and page size.
        """
        assert all(isinstance(i, int) for i in (page, page_size))
        assert all(i > 0 for i in (page, page_size))

        dataset = self.dataset()

        start_index, end_index = self.index_range(page, page_size)
        try:
            return dataset[start_index:end_index]
        except IndexError:
            return []
