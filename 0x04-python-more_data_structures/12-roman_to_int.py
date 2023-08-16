#!/usr/bin/python3
def roman_to_int(roman_string):
    sum, i = 0, 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev_value = 0

    for char in reversed(roman_string):
        if char not in roman_num:
            return 0
        value = roman_num[char]
        if value < prev_value:
            sum -= value
        else:
            sum += value
        prev_value = value
    return sum
