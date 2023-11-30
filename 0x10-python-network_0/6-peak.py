#!/usr/bin/python3
"""Finds peak in unsorted list of ints"""


def find_peak(list_of_integers):
    """Finds peak unsorted list of ints"""
    if type(list_of_integers) is not list:
        return
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
