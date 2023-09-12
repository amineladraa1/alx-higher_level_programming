#!/usr/bin/python3
"""defines a function to write in a file"""


def write_file(filename="", text=""):
    """writes to file"""
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
