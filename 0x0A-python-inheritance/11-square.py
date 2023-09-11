#!/usr/bin/python3
"""defines a Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square."""

    def __init__(self, size):
        """validate if it's an int"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def __str__(self):
        """costum string to print"""
        return "[Square] {}/{}".format(self.__size, self.__size)
