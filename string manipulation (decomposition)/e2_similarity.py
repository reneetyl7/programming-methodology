"""
File: similarity.py (extension)
Name: Renee
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    dna = input("Please give me a DNA sequence to search: ").upper()
    match = input("What DNA sequence would you like to match? ").upper()
    print("The best match is " + str(find(dna, match).upper()))


def find(dna, match):
    """
    Find the most similar subsequence in a long DNA sequence to a given short DNA sequence.
    param dna: The long DNA sequence to search in
    param match: The short DNA sequence to search for

    return:  most_similar_subsequence
    """
    max_similarity = 0
    most_similar_subsequence = ""

    # Iterate through all possible subsequences in the long sequence
    # The range ensures we don't go out of bounds
    for i in range(len(dna) - len(match) + 1):
        # Extract a subsequence of the same length as the short sequence
        subsequence = dna[i:i + len(match)]
        # Calculate similarity between this subsequence and the short sequence
        similarity = sum(a.upper() == b.upper() for a, b in zip(subsequence, match))
        similarity_percentage = (similarity / len(match)) * 100

        if similarity_percentage > max_similarity:
            max_similarity = similarity_percentage
            most_similar_subsequence = subsequence

    # Return the best match found
    return most_similar_subsequence


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
