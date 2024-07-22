#!/usr/bin/env python3
"""0-simple_helper_function"""


def index_range(page, page_size):
    """Return the tuple of start and end indices"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
