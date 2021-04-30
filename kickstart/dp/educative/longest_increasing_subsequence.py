"""
Given a number sequence, find the length of its Longest Increasing Subsequence
(LIS). In an increasing subsequence, all the elements are in increasing order
(from lowest to highest).

Example 1:
    Input: {4,2,3,6,10,1,12}
    Output: 5
    Explanation: The LIS is {2,3,6,10,12}.

Example 1:
    Input: {-4,10,3,7,15}
    Output: 4
    Explanation: The LIS is {-4,3,7,15}.
"""
from types import SimpleNamespace

def longest_increasing_subsequence_rec(input: list):

    def helper(cur: int, prev: int):
        if cur == len(input):
            return 0

        start_match = 0
        if prev < 0 or input[cur] > input[prev]:
            print("Inside the block => ", cur, prev)
            start_match = 1 + helper(cur + 1, cur)

        print("Outside the block => ", cur, prev)
        end_match: int = helper(cur + 1, prev)
        print("Final Result", start_match, end_match)
        return max(start_match, end_match)

    print(helper(0, -1))




print(longest_increasing_subsequence_rec([4, 2, 3, 6, 10, 1, 12]))
print(longest_increasing_subsequence_rec([-4, 10, 3, 7, 15]))
