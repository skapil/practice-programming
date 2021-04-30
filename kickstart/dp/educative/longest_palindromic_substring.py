"""
Given a string, find the length of its Longest Palindromic Substring (LPS).
In a palindromic string, elements read the same backward and forward.

Example 1:
    Input: "abdbca"
    Output: 3
    Explanation: LPS is "bdb".
    Example 2:

    Input: = "cddpd"
    Output: 3
    Explanation: LPS is "dpd".
    Example 3:

    Input: = "pqr"
    Output: 1
    Explanation: LPS could be "p", "q" or "r".
"""
from types import SimpleNamespace


def is_palindrom(seq: str):
    start, end = 0, len(seq) - 1
    while start <= end:
        if seq[start] != seq[end]:
            return False
        start += 1
        end -= 1
    return True


def longest_palindromic_substring_rec(seq: str):
    result = SimpleNamespace(palindrom="", length=0)

    def helper(start_index: int, end_index: int):
        if start_index == len(seq) and end_index == len(seq):
            return

        if end_index == len(seq) + 1:
            helper(start_index + 1, start_index + 1)
        else:
            sub_seq: str = seq[start_index: end_index]
            if len(sub_seq) > result.length and is_palindrom(sub_seq):
                result.palindrom, result.length = sub_seq, len(sub_seq)
            helper(start_index, end_index + 1)

    helper(0, 1)
    print(result)


def longest_palindromic_substring_dp(seq: str):
    table: List[List[int]] = [[False for x in range(len(seq))] for y in range(len(seq))]
    result: int = 1

    for row in range(len(table)):
        table[row][row] = True

    for row in range(len(table) - 1, -1, -1):
        for col in range(row + 1, len(table[row])):
            if seq[row] == seq[col] and (col - row == 1 or table[row + 1][col - 1]):
                table[row][col] = True
                result = max(result, col - row + 1)
    return result


print(longest_palindromic_substring_dp("abdbca"))
print(longest_palindromic_substring_dp("cddpd"))
print(longest_palindromic_substring_dp("pqr"))
