"""
File: hailstone.py
Name: Renee
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Make sure the number is bigger than 1, if > 1 enter the counting part
    (is_number function)
    """
    print("This program computes Hailstone sequences.", end='\n\n')
    n = int(input("Enter a number: "))
    count = 0

    if n > 1:
        while n > 1:
            n = is_number(n)  # put n inside the function!!!
            count += 1
        print("It took " + str(count) + " steps to reach 1.")

    elif n == 1:
        print("It took 0 steps to reach 1.")
    else:
        print("Can't enter Hailstone sequences.")


def is_number(n):
    """
    check the odd and even number and count
    """
    if n % 2 == 0:
        even_formula = int(n / 2)
        number1 = n
        print(str(number1) + " is even, so I take half: " + str(even_formula))
        return even_formula
    else:
        odd_formula = 3 * n + 1
        number1 = n
        print(str(number1) + " is odd, so I make 3n+1: " + str(odd_formula))
        return odd_formula


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
    main()
