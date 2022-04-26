#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = number % 10
elif number < 0:
    lastDigit = ((number * -1) % 10) * -1

if lastDigit == 0:
    str = 'Last digit of {} is {} and is 0'
elif lastDigit > 5:
    str = 'Last digit of {} is {} and is greater than 5'
elif lastDigit < 6 and lastDigit != 0:
    str = 'Last digit of {} is {} and is less than 6 and not 0'

print(f"{number, lastDigit}")
