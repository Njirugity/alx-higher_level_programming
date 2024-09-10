#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = abs(number) % 10
if number < 0:
	i = -i
if i > 5:
	print(f"Last digit of {number:d} is {i:d} and is greater than 5")
elif i == 0:
	print(f"Last digit of {number:d} is {i:d} and is 0")
else:
	print(f"Last digit of {number:d} is {i:d} and is less than 6 and not 0")
