#!/usr/bin/env python3

"""
Pagination Server Module

This module provides a simple server class to paginate a dataset of popular
baby names. It reads the data from a CSV file, caches it, and allows users to
retrieve specific pages of data based on a given page number and page size.

Classes:
    - Server: Handles the loading and pagination of the baby names dataset.

Functions:
    - dataset() -> List[List]: Returns the cached dataset, loading it from
      the CSV file if necessary.
    - index_range(page: int, page_size: int) -> Tuple[int, int]: Computes the
      start and end indices for pagination.
    - get_page(page: int, page_size: int) -> List[List]: Retrieves a specific
      page of data from the dataset.
    - get_hyper(page: int, page_size: int) -> dict: Retrieves a specific page
      of data along with hypermedia metadata.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


class Server:
    """Server: Handles the loading and pagination of the baby names dataset."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server instance, with the dataset initially
        set to None.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the cached dataset.

        If the dataset is not already loaded, it reads the data from the
        'Popular_Baby_Names.csv' file, skipping the header row, and caches it.

        Returns:
            List[List]: The dataset as a list of lists, where each inner list
            represents a row in the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Computes the start and end indices for a given page and page size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Tuple[int, int]: A tuple containing the start and end indices
            for the dataset.
        """
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        This method uses the `index_range` method to calculate the correct
        slice of the dataset based on the page number and page size.

        Args:
            page (int, optional): The page number to retrieve (default is 1).
            page_size (int, optional): The number of items per page
            (default is 10).

        Returns:
            List[List]: The list of rows for the specified page. If the page
            number is out of range, an empty list is returned.

        Raises:
            AssertionError: If `page` or `page_size` is not a positive integer.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = self.index_range(page, page_size)
        dataset = self.dataset()

        try:
            return dataset[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieves a specific page of data along with hypermedia metadata.

        This method provides pagination data in a format that includes
        additional metadata like the total number of pages, next page, and
        previous page links.

        Args:
            page (int, optional): The page number to retrieve (default is 1).
            page_size (int, optional): The number of items per page
            (default is 10).

        Returns:
            Dict[str, Any]: A dictionary containing the following keys:
                - page_size: The number of items on the current page.
                - page: The current page number.
                - data: The list of rows for the current page.
                - next_page: The next page number if it exists, else None.
                - prev_page: The previous page number if it exists, else None.
                - total_pages: The total number of pages in the dataset.
        """
        data = self.get_page(page, page_size)
        total_pages = (len(self.dataset()) + page_size - 1) // page_size

        metadata = {
                "page_size": (page_size if page_size <= len(data) else
                              len(data)),
                "page": page,
                "data": data,
                "next_page": page + 1 if page < data else None,
                "prev_page": page - 1 if page > 0 else None,
                "total_pages": total_pages
        }

        return metadata
