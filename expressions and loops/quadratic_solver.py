"""
File: quadratic_solver.py
Name: Renee
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	One step to the end of the answer
	"""
	print("Quadratic Solver!")
	a = float(input("Enter a: "))
	b = float(input("Enter b: "))
	c = float(input("Enter c: "))

	root_check = b*b - 4*a*c

	if root_check > 0:
		answer = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
		answer1 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
		print("Two roots: " + str(answer) + "," + str(answer1))
	elif root_check == 0:
		answer = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
		print("One root: " + str(answer))
	else:
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
