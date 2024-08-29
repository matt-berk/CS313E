"""
DNA
"""
# File: dna.py

# Description

# Student Name: Matthew Berk

# Student UT EID: mb67665

# Partner Name: Charles Ruhman

# Partner UT EID:

# Course Name: CS 313E

# Unique Number:

# Date Created:  8/28/2024

# Date Last Modified: 8/28/2024

# Input: string_1 and string_2 are two strings that represent strands of DNA.
# Output: returns a sorted list of substrings that are the longest common subsequence.
#         The list is empty if there are no common subsequences.


def longest_subsequence(string_1, string_2):
    """ADD YOUR CODE HERE """
    string_1 = string_1.upper()
    string_2 = string_2.upper()
    longest_subs = []
    max_length = 0

    #Finding all common subsequences
    for i in range(len(string_1)):
        for j in range(i + 1, len(string_1) + 1):
            subseq = string_1[i:j]
            if subseq in string_2:
                if len(subseq) > max_length:
                    longest_subs = [subseq]
                    max_length = len(subseq)
                elif len(subseq) == max_length:
                    longest_subs.append(subseq)
    longest_subs = sorted(set(longest_subs))
    return longest_subs





def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
