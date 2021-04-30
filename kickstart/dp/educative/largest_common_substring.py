"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest substring
which is common in both the strings.

Example 1:
    Input: s1 = "abdca"
           s2 = "cbda"
    Output: 2
    Explanation: The longest common substring is "bd".

Example 2:
    Input: s1 = "passport"
           s2 = "ppsspt"
    Output: 3
    Explanation: The longest common substring is "ssp".
"""
from collections import defaultdict

def find_longest_substring_rec(first: str, second: str):

    def helper(first_index: int, second_index: int, count: int):
        if first_index >= len(first) or second_index >= len(second):
            return count

        if first[first_index] == second[second_index]:
            count = helper(first_index + 1, second_index + 1, count + 1)

        match_first = helper(first_index, second_index + 1, 0)
        match_second = helper(first_index + 1, second_index, 0)

        return max(count, max(match_first, match_second))

    return helper(0, 0, 0)


def find_longest_substring_memo(first: str, second: str):
    memo: DefaultDict = defaultdict(int);

    def helper(first_index: int, second_index: int, count: int):
        if first_index >= len(first) or second_index >= len(second):
            return count

        key: str = f"{first_index}|{second_index}|{count}"
        if f"{first_index}|{second_index}|{count}" not in memo:
            match_point: int = count
            if first[first_index] == second[second_index]:
                match_point = helper(first_index + 1, second_index + 1, count + 1)

            match_first = helper(first_index, second_index + 1, 0)
            match_second = helper(first_index + 1, second_index, 0)
            key: str = f"{first_index}|{second_index}|{count}"
            memo[key] = max(match_point, max(match_first, match_second))
        return memo[key]

    result: int = helper(0, 0, 0)
    print(memo)
    return result

def find_longest_substring_dp(first: str, second: str) -> int:
    table: List[List[int]] = [[0 for x in range(len(second))] for y in range(len(first))]

    for col in range(len(table[0])):
        if first[0] == second[col]:
            table[0][col] = 1

    for row in range(len(table)):
        if first[row] == second[0]:
            table[row][0] = 1

    longest: int = 0
    for row in range(1, len(table)):
        for col in range(1, len(table[row])):
            if first[row] == second[col]:
                table[row][col] = 1 + table[row - 1][col - 1]
                longest = max(longest, table[row][col])

    print(table)
    return longest

def main():
    print(find_longest_substring_dp("abdca", "cbda"))
    print(find_longest_substring_dp("passport", "ppsspt"))


main()
