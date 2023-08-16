#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    intSum = 0
    t_weight = 0
    for score, weight in my_list:
        intSum += score * weight
        t_weight += weight
    if t_weight == 0:
        return 0
    return intSum / t_weight
