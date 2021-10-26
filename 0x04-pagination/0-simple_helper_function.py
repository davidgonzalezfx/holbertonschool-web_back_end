#!/usr/bin/env python3
""" Learning Pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Simple helper function """

    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
