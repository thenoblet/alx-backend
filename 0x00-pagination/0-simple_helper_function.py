#!/usr/bin/env python3
"""
Pagination Utility

This module provides a utility function to calculate the start and end indices
for pagination, which is useful for breaking down a large dataset into
manageable pages.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of size two containing a start index and an end index.

    The start index is inclusive and calculated as (page - 1) * page_size.
    The end index is exclusive and calculated as start + page_size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
