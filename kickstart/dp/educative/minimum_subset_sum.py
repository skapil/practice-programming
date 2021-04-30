"""
Given a set of positive numbers, partition the set into two subsets with
a minimum difference between their subset sums.

Example 1: #
    Input: {1, 2, 3, 9}
    Output: 3
    Explanation:
        We can partition the given set into two subsets where minimum absolute
        difference between the sum of numbers is '3'.
        Following are the two subsets: {1, 2, 3} & {9}.

Example 2: #
    Input: {1, 2, 7, 1, 5}
    Output: 0
    Explanation:
    We can partition the given set into two subsets where minimum absolute
    difference between the sum of number is '0'.
    Following are the two subsets: {1, 2, 5} & {7, 1}.

Example 3: #
    Input: {1, 3, 100, 4}
    Output: 92
    Explanation:
    We can partition the given set into two subsets where minimum absolute
    difference between the sum of numbers is '92'.
    Here are the two subsets: {1, 3, 4} & {100}.
"""

from typing import List, DefaultDict
import math
import pprint
from types import SimpleNamespace
from collections import defaultdict


def minimum_absolute_difference_rec(nums: list) -> List[List[int]]:
    result: list = []
    max_sum: int = sum(nums)
    min_diff = SimpleNamespace(value=math.inf)

    def helper(slate: list, idx: int, cur_sum: int, max_sum: int):
        cur_diff: int = (max_sum - cur_sum) - cur_sum
        if len(slate) < len(nums) and cur_diff >= 0 and cur_diff < min_diff.value:
            min_diff.value = cur_diff
            result.clear()
            result.extend(list(slate))

        if idx >= len(nums):
            return

        slate.append(idx)
        helper(slate, idx + 1, cur_sum + nums[idx], max_sum)
        slate.pop()
        helper(slate, idx + 1, cur_sum, max_sum)

    helper([], 0, 0, max_sum)
    results: List[List[int]] = get_partitions_array(nums, result)
    return results


def minimum_absolute_difference_memo(nums: list) -> List[List[int]]:
    result: list = []
    max_sum: int = sum(nums)
    min_diff: int = SimpleNamespace(value=math.inf)
    memo: DefaultDict = defaultdict(list)

    def helper(slate: list, idx: int, cur_sum: int, max_sum: int):
        cur_diff: int = (max_sum - cur_sum) - cur_sum
        if len(slate) < len(nums) and cur_diff >= 0 and cur_diff < min_diff.value:
            min_diff.value = cur_diff
            result.clear()
            result.extend(list(slate))

        if idx >= len(nums):
            return

        if idx not in memo:
            slate.append(idx)
            memo[idx].append(list(slate))
            helper(slate, idx + 1, cur_sum + nums[idx], max_sum)
            slate.pop()
        if idx not in memo:
            memo[idx].append(list(slate))
            helper(slate, idx + 1, cur_sum, max_sum)

    helper([], 0, 0, max_sum)
    results: List[List[int]] = get_partitions_array(nums, result)
    return results


def get_partitions_array(nums: list, first_partition: list) -> List[List[int]]:
    second_partition: list = []
    first_idx: int = 0

    for index in range(len(nums)):
        if first_idx >= len(first_partition):
            second_partition.append(index)
        elif index != first_partition[first_idx]:
            second_partition.append(index)
        else:
            first_idx += 1

    return [first_partition, second_partition]


def minimum_absolute_difference_dp(nums: list) -> List[List[int]]:
    sum_nums: int = sum(nums)
    table: List[List[int]] = [[0 for x in range((sum_nums // 2) + 1)]
                              for y in range(len(nums))]

    for row in range(len(table)):
        table[row][0] = 1

    row: int = 0
    for col in range(1, len(table[0])):
        if col == nums[row]:
            table[0][col] = 1

    biggest_sum: int = 0
    for row in range(1, len(table)):
        for col in range(1, len(table[row])):
            if table[row - 1][col] or (col >= nums[row] and table[row - 1][col - nums[row]]):
                table[row][col] = 1
                biggest_sum = col

    print(table)
    print(biggest_sum)
    return abs((sum_nums - biggest_sum) - biggest_sum)


print(f"Min Difference: {minimum_absolute_difference_dp([1, 2, 3, 9])}")
print(f"Min Difference: {minimum_absolute_difference_dp([1, 2, 7, 1, 5])}")
print(f"Min Difference: {minimum_absolute_difference_dp([1, 3, 100, 4])}")
