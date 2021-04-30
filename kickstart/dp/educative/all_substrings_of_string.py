"""
Given a string, find the length of its Longest Palindromic Substring (LPS).
In a palindromic string, elements read the same backward and forward.

Example 1:
    Input: "abdbca"
    Output: 3
    Explanation: LPS is "bdb"

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


def get_longest_palindromic_substring_rec(seq: str):
    result = SimpleNamespace(sub_string="", length=0)

    def helper(start_index: int, end_index: int):
        if start_index == len(seq) and end_index == len(seq):
            return
        if end_index == len(seq) + 1:
            print("I am here now", start_index, end_index)
            helper(start_index + 1, start_index + 1)
        else:
            print(start_index, end_index)
            print(seq[start_index: end_index])
            helper(start_index, end_index + 1)

    helper(0, 1)


print(get_longest_palindromic_substring_rec("abdbca"))
print(get_longest_palindromic_substring_rec("cddpd"))
print(get_longest_palindromic_substring_rec("pqr"))
