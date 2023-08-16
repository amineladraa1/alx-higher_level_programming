#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    u_set1 = set_1 - set_2
    u_set2 = set_2 - set_1
    return u_set1.union(u_set2)
