"""
Given a string, find the total number of palindromic substrings in it.
Please note we need to find the total number of substrings and not subsequences.

Example 1:
    Input: "abdbca"
    Output: 7
    Explanation: Here are the palindromic substrings,
        "a", "b", "d", "b", "c", "a", "bdb".

Example 2:
    Input: = "cddpd"
    Output: 7
    Explanation: Here are the palindromic substrings,
        "c", "d", "d", "p", "d", "dd", "dpd".

Example 3:
    Input: = "pqr"
    Output: 3
    Explanation: Here are the palindromic substrings,"p", "q", "r".
"""
from types import SimpleNamespace


def is_palindrom(seq: str):
    start, end = 0, len(seq) - 1
    while start < end:
        if seq[start] != seq[end]:
            return False
        start += 1
        end -= 1
    return True


def count_number_palindrom_rec(seq: str):
    result = SimpleNamespace(palindrom=[], count=0)

    def helper(start: int, end: int):
        if start == len(seq) and end == len(seq):
            return
        if end == len(seq) + 1:
            helper(start + 1, start + 1)
        else:
            sub_seq: str = seq[start: end]
            if sub_seq and is_palindrom(sub_seq):
                result.palindrom.append(sub_seq)
                result.count += 1
            helper(start, end + 1)

    helper(0, 1)
    print(result)


def count_number_palindrom_dp(seq: str):
    table: List[List[int]] = [[0 for x in range(len(seq))] for y in range(len(seq))]

    count = 1
    for row in range(len(table)):
        table[row][row] = count
        count += 1

    for row in range(len(table) - 1, -1, -1):
        for col in range(row + 1, len(table)):
            if seq[row] == seq[col]:
                table[row][col] = 1 + table[row + 1][col]
            else:
                table[row][col] = max(table[row + 1][col], table[row][col - 1])
    return table[0][-1]


print(count_number_palindrom_dp("abdbca"))
print(count_number_palindrom_dp("cddpd"))
print(count_number_palindrom_dp("pqr"))
