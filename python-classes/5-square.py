#!/usr/bin/python3
# 5-square.py

"""Def une Instance area."""


class Square:
    """Représente une Instance area = size**2."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Renvoie l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """Renvoie un carré à partir de l'aire"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__size * "#")
