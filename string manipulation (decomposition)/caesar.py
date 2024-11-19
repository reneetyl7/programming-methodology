"""
File: caesar.py
Name: Renee
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
import string

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    num = input("Secret number: ")
    if not num.isdigit():
        print("Error: Secret number must be an integer.")
        return
    s = input("What's the ciphered string? ")
    # Uppercase checker
    s2 = s.upper()
    new_a = switch_s(ALPHABET, num)
    ans = find_w(new_a, s2)
    print("The deciphered string is: " + ans)


def switch_s(alphabet, num):
    """
    Rearranges the alphabet based on the secret number.

    Param alphabet (str): The original alphabet.
    Param num (str): The secret number used to rearrange the alphabet.

    Returns:
    str: The rearranged alphabet.
    """
    num = int(num)
    num = num % len(alphabet)  # Ensure num is within the range of the alphabet length
    p1 = alphabet[(26-num):]
    p2 = alphabet[:(25-num)]
    new_a = p1 + p2
    return new_a


def find_w(new_a, s2):
    """
    Deciphers the string using the rearranged alphabet.

    Param new_a (str): The rearranged alphabet.
    Param s (str): The ciphered string to be deciphered.

    Returns:
    str: The deciphered string.
    """
    ans = ''
    for char in s2:
        if char.isalpha():
            i = new_a.find(char)
            ans += ALPHABET[i]
        else:
            ans += char
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
