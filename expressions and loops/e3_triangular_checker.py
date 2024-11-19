"""
File: extension3_triangular_checker.py
Name: Renee
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    print("Welcome to the triangular number checker!")
    while True:
        n = int(input("n: "))

        if n == EXIT:
            print("Have a good one!")
            break

        if n < 0:
            print("It does not include the number!")

        if n == 0 or n == 1:
            print(str(n) + " is a triangular number")

        tri_sum = 0
        for i in range(n):
            tri_sum += i
            if tri_sum == n:
                print(str(n) + " is a triangular number")
                break
            elif tri_sum > n:
                print(str(n) + " is not a triangular number")
                break


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
