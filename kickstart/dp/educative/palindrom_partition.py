"""
Given a string, we want to cut it into pieces such that each piece is a
palindrome. Write a function to return the minimum number of cuts needed.

    Example 1:
    Input: "abdbca"
    Output: 3
    Explanation: Palindrome pieces are "a", "bdb", "c", "a".

Example 2:
    Input: = "cddpd"
    Output: 2
    Explanation: Palindrome pieces are "c", "d", "dpd".

Example 3:
    Input: = "pqr"
    Output: 2
    Explanation: Palindrome pieces are "p", "q", "r".

Example 4:
    Input: = "pp"
    Output: 0
    Explanation: We do not need to cut, as "pp" is a palindrome.
"""


def find_MPP_cuts(st):
    return find_MPP_cuts_recursive(st, 0, len(st) - 1)


def find_MPP_cuts_recursive(st, startIndex, endIndex):
    # we don't need to cut the string if it is a palindrome
    if startIndex >= endIndex or is_palindrome(st, startIndex, endIndex):
        return 0

    # at max, we need to cut the string into its 'length-1' pieces
    minimumCuts = endIndex - startIndex
    for i in range(startIndex, endIndex + 1):
        print(st[startIndex: i + 1], i, startIndex, endIndex, minimumCuts)
        if is_palindrome(st, startIndex, i):
            # we can cut here as we have a palindrome from 'startIndex' to 'i'
            minimumCuts = min(
                minimumCuts, 1 + find_MPP_cuts_recursive(st, i + 1, endIndex))

    return minimumCuts


def get_substring(seq: str):
    substrings: list = []

    def helper(start: int, end: int):
        if start >= end:
            if start == end and start < len(seq):
                substrings.append(seq[start: end + 1])
            return
        for index in range(start, end + 1):
            substrings.append(seq[start: index + 1])
            helper(index + 1, end)

    helper(0, len(seq) - 1)
    print(substrings)


def is_palindrome(st, x, y):
    while (x < y):
        if st[x] != st[y]:
            return False
        x += 1
        y -= 1
    return True


def main():
    get_substring("pqr")
    # print(find_MPP_cuts("abdbca"))
    # print(find_MPP_cuts("cdpdd"))
    # print(find_MPP_cuts("pqr"))
    # print(find_MPP_cuts("pp"))
    # print(find_MPP_cuts("madam"))


main()
