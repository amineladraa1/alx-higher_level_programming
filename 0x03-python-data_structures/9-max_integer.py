#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    highest = my_list[0]
    for d in my_list:
        if d > highest:
            highest = d
    return highest
