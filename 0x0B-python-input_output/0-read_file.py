#!/usr/bin/python3
"""define a function to read a file"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding="UTF-8") as f:
        for f_line in f:
            print("{}".format(f_line))
