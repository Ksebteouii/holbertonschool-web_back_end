#!/usr/bin/env python3
"""Python function that lists all documents in a collection with comments"""

import pymongo


def list_all(mongo_collection):
    """
    This function lists all documents in a given MongoDB collection.

    """

    # Check if the collection is None, and return an empty list if it is.
    if mongo_collection is None:
        return []

    # Use the find() method to retrieve all documents in the collection.
    return mongo_collection.find()
