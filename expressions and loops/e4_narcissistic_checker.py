"""
File: extension4_narcissistic_checker.py
Name: Renee
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    print("Welcome to the narcissistic number checker!")
    while True:
        n = int(input("n: "))

        if n == EXIT:
            print("Have a good one!")
            break

        #  Check if a number is narcissistic
        if is_narcissistic(n):
            print(str(n) + " is a narcissistic number")
        else:
            print(str(n) + " is not a narcissistic number")


def count_digits(n):
    """Function to count the number of digits in a number"""
    count = 0
    while n:
        n //= 10
        count += 1
    return count


def is_narcissistic(n):
    """Function to check if a number is narcissistic"""
    original_n = n
    sum_of_digits = 0
    num_digits = count_digits(n)
    for i in range(num_digits):
        digit = n % 10
        sum_of_digits += digit ** num_digits
        n //= 10
    return sum_of_digits == original_n


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
