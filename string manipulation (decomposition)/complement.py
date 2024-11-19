"""
File: complement.py
Name: Renee
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    Builds the complementary DNA strand of the given DNA sequence.
    If the input DNA sequence is an empty string, the function will print a message and
    return the original empty string.

    Args:
        dna (str): The input DNA sequence.

    Returns:
        str: The complementary DNA strand.
    """
    if dna == '':
        return "DNA strand is missing."
    else:
        ans = ''
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                ans += 'T'
            elif ch == 'C':
                ans += 'G'
            elif ch == 'G':
                ans += 'C'
            else:
                ans += 'A'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
