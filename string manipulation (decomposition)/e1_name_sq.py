"""
File: name_sq.py (extension)
Name: Renee
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    print("This program prints a name in a square pattern!")
    name = input("Name: ")
    # Get the length of the name
    length = len(name)

    # Print the top row
    print(name)

    # Print middle rows
    for i in range(1, length - 1):
        print(name[i] + ' ' * (length - 2) + name[length - i - 1])

    # Print the bottom row (reversed name)
    if length > 1:
        print(name[::-1])


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
