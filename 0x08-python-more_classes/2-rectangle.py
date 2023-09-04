#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise TypeError("width must be >= 0")

        @property
        def height(self):
            return self.height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")

        def area(self):
            return self.width * self.height

        def perimeter(self):
            if self.__width == 0 or self.__height == 0:
                return (0)
            return (self.__width * 2) + (self.__height * 2)
