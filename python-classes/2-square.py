#!/usr/bin/python3
# 2-square.py

"""Def une Instance size = 0."""


class Square:
    """Représente une Instance size = 0."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
