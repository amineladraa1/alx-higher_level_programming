#!/usr/bin/python3
def best_score(a_dictionary):
    highest = 0
    key = ""
    if a_dictionary == None:
        return None
    for k, v in a_dictionary.items():
        if v > highest:
            highest = v
            key = k
        else:
            continue
    return key
