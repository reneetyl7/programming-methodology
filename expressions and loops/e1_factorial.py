"""
File: extension1_factioral.py
Name: Renee
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100  # Set the exit


def main():
	print("Welcome to factorial master!")
	while True:
		n = int(input("Give me a number, and I will list the answer of factorial: "))

		if n == EXIT:
			print("- - - - - - See ya! -------------")
			break

		factorial = 1
		if n >= 1:
			for i in range(1, n+1):
				factorial = factorial * i
			print("Answer: " + str(factorial))


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
	main()
