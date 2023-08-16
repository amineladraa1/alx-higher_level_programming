#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    sort_k = sorted(a_dictionary)
    for k in sort_k:
        print("{}: {}".format(k, a_dictionary[k]))
