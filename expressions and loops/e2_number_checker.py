"""
File: extension2_number_checker.py
Name: Renee
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -100  # Set the exit


def main():
    print("Welcome to the number checker!")
    while True:
        n = int(input("n: "))

        if n == EXIT:
            print("Have a good one!")
            break

        sum_div = 0
        for i in range(1, n):  # if the number is in the n, then count
            if n % i == 0:     # if n can be divided by number
                sum_div += i   # add the number together

        if sum_div == n:
            print(str(n) + " is a perfect number")
        elif sum_div > n:
            print(str(n) + " is an abundant number")
        elif sum_div < n:
            print(str(n) + " is a deficient number")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
