#!/usr/bin/python3
"""Defines an object attribute lookup function."""

def lookup(obj):
    """return a list of attributes"""
    return dir(obj)
