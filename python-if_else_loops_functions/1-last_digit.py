#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if (last > 5):
    numProperty = "greater than 5"
elif ((last < 6) and (last != 0)):
    numProperty = "less than 6 and not 0"
elif (last == 0):
    numProperty = "0"
if (number < 0):
    last *= -1
print(f"Last digit of {number} is {last} and is {numProperty}")
