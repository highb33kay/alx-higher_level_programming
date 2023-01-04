#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
	x = -1 * (- number % 10)
else:
	x = number % 10

if x > 5:
	print("Last digit of {:d} is {:d} and is greater than 5".format(number, x))
elif x == 0:
	print("Last digit of {:d} is {:d} and is equal to 0".format(number, x))
elif x < 6 and x != 0:
	print("Last digit of {:d} is {:d}".format(number, x), end= " ")
	print("and is not equal to zero.")
