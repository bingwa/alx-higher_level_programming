#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10 if number > 0 else int(repr(number)[-1]) * -1

print (f"Last digit of {number} is {lastDigit}")

if lastDigit > 5:
   
