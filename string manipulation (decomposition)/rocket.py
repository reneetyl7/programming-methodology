"""
File: rocket.py
Name: Renee
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 5


def main():
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    Prints the top part of the rocket (the head).
    The head consists of a triangle of forward and backward slashes.
    The size of the triangle is determined by the `SIZE` constant.
    """
    for i in range(SIZE):
        for j in range(SIZE - i):
            print(" ", end="")
        for j in range(i + 1):
            print("/", end="")
        for j in range(i + 1):
            print("\\""", end="")
        for j in range(SIZE - i):
            print(" ", end="")
        print(" ")


def belt():
    """
    Prints the belt part of the rocket.
    The belt consists of a row of `+` characters with `=` characters between them.
    The length of the belt is determined by the `SIZE` constant.
    """
    print("+", end="")
    for i in range(SIZE * 2):
        print("=", end="")
    print("+")


def upper():
    """
    Prints the upper part of the rocket body.
    The upper part consists of a series of vertical bars with a forward and backward slash pattern.
    The size of the pattern is determined by the `SIZE` constant.
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range((SIZE - i) - 1):
            print(".", end="")
        for j in range(i + 1):
            print("/\\""", end="")
        for j in range((SIZE - i) - 1):
            print(".", end="")
        print("|")


def lower():
    """
    Prints the lower part of the rocket body.
    The lower part consists of a series of vertical bars with a backward and forward slash pattern.
    The size of the pattern is determined by the `SIZE` constant.
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(SIZE - i):
            print("\\/""", end="")
        for j in range(i):
            print(".", end="")
        print("|")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
    main()
