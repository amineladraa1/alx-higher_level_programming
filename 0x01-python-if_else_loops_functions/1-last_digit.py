#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
if number < 0:
    lastd *= -1
tempString = ""
if lastd > 5:
    tempString = "and is greater than 5"
elif lastd == 0:
    tempString = "and is 0"
elif lastd < 6 and lastd != 0:
    tempString = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {lastd:d} {tempString}")
