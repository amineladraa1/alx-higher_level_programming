#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    intSum = 0
    for i in my_list:
        if i not in unique:
            intSum += i
            unique.add(i)
    return intSum
