#!/usr/bin/python3
"""Finds peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds Peak"""
    if not list_of_integers:
        return None

    """Peak Search"""
    b = 0
    t = len(list_of_integers) - 1
    while b < t:
        c = (b + t) // 2
        if list_of_integers[c] < list_of_integers[c + 1]:
            b = c + 1
        else:
            t = c
    return list_of_integers[b]
    