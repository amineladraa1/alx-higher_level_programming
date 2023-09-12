#!/usr/bin/python3
"""defines a function to append in a file"""


def append_write(filename="", text=""):
    """append to file"""
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
