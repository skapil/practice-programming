"""
Given strings s1 and s2, we need to transform s1 into s2 by deleting and
inserting characters. Write a function to calculate the count of the minimum
number of deletion and insertion operations.

Example 1:
    Input: s1 = "abc"
           s2 = "fbc"
    Output: 1 deletion and 1 insertion.
    Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.

Example 2:
    Input: s1 = "abdca"
           s2 = "cbda"
    Output: 2 deletions and 1 insertion.
    Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.

Example 3:
    Input: s1 = "passport"
           s2 = "ppsspt"
    Output: 3 deletions and 1 insertion
    Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.
"""
def transform_string_rec(first: str, second: str):

    def helper(first_index: int, second_index: int):
        if first_index >= len(first) or second_index >= len(second):
            return 0

        if first[first_index] == second[second_index]:
            return 1 + helper(first_index + 1, second_index + 1)

        match_first: int = helper(first_index + 1, second_index)
        match_second: int = helper(first_index, second_index + 1)
        return max(match_first, match_second)

    lcs: int = helper(0, 0)
    print("Minimum Deletion Needed: ", len(first) - lcs)
    print("Minimum Insertion Needed: ", len(second) - lcs)


transform_string_rec("abc", "fbc")
transform_string_rec("abdca", "cbda")
transform_string_rec("passport", "ppsspt")
