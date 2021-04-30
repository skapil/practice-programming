from typing import List
import pprint


def solve_knapsack(profits, weights, capacity):
    # basic check
    if capacity <= 0 or capacity == 0 or len(weights) != len(profits):
        return 0

    table: list = [[0] * (capacity + 1)] * len(profits)

    for row in range(len(table)):
        table[row][0] = 0

    for capc in range(capacity + 1):
        if capc >= weights[0]:
            table[0][capc] = profits[0]

    for row in range(len(table)):
        for col in range(len(table[row])):
            cur_profit, prev_max_profit = 0, 0
            if col >= weights[row]:
                cur_profit = (profits[row] +
                              table[row - 1][col - weights[row]])
            prev_max_profit = table[row - 1][col]
            table[row][col] = max(prev_max_profit, cur_profit)

    print(table)
    return table[-1][-1]


def get_subset_sum_table(nums: list, target: int) -> List[List[int]]:
    table: list = [[0 for x in range(target + 1)] for y in range(len(nums))]

    for col in range(len(table[0])):
        if col == nums[0]:
            table[0][col] = 1

    for row in range(len(table)):
        for col in range(1, len(table[row])):
            if table[row - 1][col] == 1:
                table[row][col] = 1
            elif nums[row] == col or table[row - 1][col - nums[row]]:
                table[row][col] = 1

    return table


def subset_sum(nums: list) -> bool:
    sum_nums: int = sum(nums)
    if len(nums) in {0, 1} or sum_nums & 1:
        return False

    table: List[List[int]] = get_subset_sum_table(nums, sum_nums // 2)
    return True if table[-1][-1] else False


def print_subset_sum_values(nums: list) -> List[bool]:
    result: List[int] = [0] * len(nums)

    target: int = sum(nums) // 2
    table: List[List[int]] = get_subset_sum_table(nums, target)
    row: int = len(table) - 1
    col: int = len(table[0]) - 1

    while row != 0 and col != 0:
        if table[row - 1][col] != 1:
            result[row] = 1
            col -= nums[row]
        else:
            row -= 1
    result[0] = 1 if table[row][col] == 1 else 0
    return result


print(print_subset_sum_values([1, 6, 10, 16]))
print(print_subset_sum_values([1, 2, 3, 4]))
print(print_subset_sum_values([1, 1, 3, 4, 7]))
print(print_subset_sum_values([2, 3, 4, 6]))
