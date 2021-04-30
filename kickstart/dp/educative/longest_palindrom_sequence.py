"""
Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
In a palindromic subsequence, elements read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements.

Example 1:
    Input: "abdbca"
    Output: 5
    Explanation: LPS is "abdba".

Example 2:
    Input: = "cddpd"
    Output: 3
    Explanation: LPS is "ddd".

Example 3:
    Input: = "pqr"
    Output: 1
    Explanation: LPS could be "p", "q" or "r".
"""
from types import SimpleNamespace


def is_palindrom(seq: str) -> bool:
    left, right = 0, len(seq) - 1
    while left <= right:
        if seq[left] != seq[right]:
            return False
        left += 1
        right -= 1
    return True


def get_max_palindrom_subsequence_rec(seq: str):
    subsequence = SimpleNamespace(max_palindrom='', length=0)

    def helper(slate: list, idx: int, seq: str):
        print(''.join(slate))
        if len(slate) > subsequence.length:
            subseq: str = ''.join(slate)
            if is_palindrom(subseq):
                subsequence.max_palindrom = ''.join(list(subseq))
                subsequence.length = len(subseq)
        if idx >= len(seq):
            return

        slate.append(seq[idx])
        helper(slate, idx + 1, seq)
        slate.pop()
        helper(slate, idx + 1, seq)

    helper([], 0, seq)
    return subsequence


def get_max_palindrom_subsequence_rec_2(seq: str, start: int, end: int):
    if start > end:
        return 0

    if start == end:
        return 1

    if seq[start] == seq[end]:
        return 2 + get_max_palindrom_subsequence_rec_2(seq, start + 1, end - 1)

    first_lps: int = get_max_palindrom_subsequence_rec_2(seq, start + 1, end)
    second_lps: int = get_max_palindrom_subsequence_rec_2(seq, start, end - 1)
    return max(first_lps, second_lps)


def get_max_palindrom_subsequence_dp(seq: str):
    table: List[List[int]] = [[0 for x in range(len(seq))] for y in range(len(seq))]

    for row in range(len(table)):
        table[row][row] = 1

    for row in range(len(seq) - 1, -1, -1):
        for col in range(row + 1, len(seq)):
            if seq[row] == seq[col]:
                table[row][col] = 2 + table[row + 1][col - 1]
            else:
                table[row][col] = max(table[row][col - 1], table[row + 1][col])

    return table[0][-1]


print(get_max_palindrom_subsequence_dp("abdbca"))
print(get_max_palindrom_subsequence_dp("cddpd"))
print(get_max_palindrom_subsequence_dp("pqr"))
