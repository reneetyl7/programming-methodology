"""
File: string_score.py
Name: Renee
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    print(score('1aB4rC'))    # digit->1 ; upper->2; lower->3
    # 12
    print(score('aaaaA3'))
    # 15


def score(string):
    """
    Calculates the score of a given string based on the following rules:
    - Each digit character (0-9) contributes 1 point.
    - Each uppercase letter contributes 2 points.
    - Each lowercase letter contributes 3 points.

    Args:
        string (str): The input string to be scored.

    Returns:
            int: The total score of the input string.
    """

    ans = 0
    for i in range(len(string)):
        ch = string[i]
        if ch.isdigit():
            ans += 1
        elif ch.isupper():
            ans += 2
        else:
            ans += 3
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()