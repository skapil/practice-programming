"""
Given a set of positive numbers, determine if there exists a subset whose
sum is equal to a given number ‘S’.

Example 1: #
    Input: {1, 2, 3, 7}, S=6
    Output: True
    The given set has a subset whose sum is '6': {1, 2, 3}

Example 2: #
    Input: {1, 2, 7, 1, 5}, S=10
    Output: True
    The given set has a subset whose sum is '10': {1, 2, 7}

Example 3: #
    Input: {1, 3, 4, 8}, S=6
    Output: False
    The given set does not have any subset whose sum is equal to '6'.
"""

from typing import List, DefaultDict
from collections import defaultdict
import pprint


def can_partition_rec(nums: list, target: int) -> bool:
    result: list = []

    def helper(slate: list, idx: int, cur_sum: int, target: int) -> bool:
        if cur_sum > target:
            return False
        if cur_sum == target:
            result.extend(list(slate))
            return True
        if idx >= len(nums):
            return False

        slate.append(nums[idx])
        if helper(slate, idx + 1, cur_sum + nums[idx], target):
            return True
        slate.pop()
        if helper(slate, idx + 1, cur_sum, target):
            return True
        return False

    is_subset_sum: bool = helper([], 0, 0, target)
    print(result)
    return True if is_subset_sum else False


def can_partition_memo(nums: list, target: int) -> bool:
    result: list = []
    memo: DefaultDict = defaultdict(list)

    def helper(slate: list, idx: int, cur_sum: int, target: int) -> bool:
        if cur_sum > target:
            return False
        if cur_sum == target:
            result.extend(list(slate))
            return True
        if idx >= len(nums):
            return False

        if nums[idx] not in memo:
            slate.append(nums[idx])
            memo[nums[idx]].append(list(slate))
            if helper(slate, idx + 1, cur_sum + nums[idx], target):
                return True
            slate.pop()
        if nums[idx] not in memo:
            memo[nums[idx]].append(list(slate))
            if helper(slate, idx + 1, cur_sum, target):
                return True

        return False

    is_subset_sum: bool = helper([], 0, 0, target)
    print(result)
    print(memo)
    return True if is_subset_sum else False


def can_partition_dp(nums: list, target: int) -> bool:
    table: list = [[0 for x in range(target + 1)] for y in range(len(nums))]

    for col in range(len(nums)):
        if nums[0] == col:
            table[0][col] = 1
            break

    for row in range(1, len(table)):
        for col in range(1, len(table[0])):
            if (table[row - 1][col] or col == nums[row] or
                    (col - nums[row] >= 0 and table[row - 1][col - nums[row]])):
                table[row][col] = 1

    pprint.pprint(table)
    if table[-1][-1]:
        return get_subset_values(nums, table)
    return []


def get_subset_values(nums: list, table: List[List[int]]) -> list:
    result: list = []
    row: int = 0
    col: int = 0

    for row in range(len(nums)):
        if not table[row - 1][col]:
            result.append(nums[row])
            col -= nums[row]
        else:
            row -= 1
    if row >= 0 and col >= 0 and table[row][col]:
        result.append(nums[row])

    return result


print("Can partition: " + str(can_partition_dp([1, 2, 3, 7], 6)))
print("Can partition: " + str(can_partition_dp([1, 2, 7, 1, 5], 10)))
print("Can partition: " + str(can_partition_dp([1, 3, 4, 8], 6)))
