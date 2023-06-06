#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
   n = -n
if n > 5:
   print(f"Last digit of {number} is {n} and it is greater than 5")
elif n < 6 and n != 0:
   print(f"Last digit of {number} is {n} and it is less than 6 and not 0")
else:
   print(f"Last digit of {number} is {n} and is 0")
