#!/usr/bin/env python3
""" returns a function that multiplies a float by multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by multiplier"""

    def multiply(number: float) -> float:
        """multiplies a float by multiplier"""
        return number * multiplier

    return multiply
