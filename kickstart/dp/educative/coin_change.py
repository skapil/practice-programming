"""
Given an infinite supply of ‘n’ coin denominations and a total money amount,
we are asked to find the total number of distinct ways to make up that amount.

Example:
=========================
Denominations: {1,2,3}
Total amount: 5
Output: 5
Explanation: There are five ways to make the change for '5', here are those ways:
  1. {1,1,1,1,1}
  2. {1,1,1,2}
  3. {1,2,2}
  4. {1,1,3}
  5. {2,3}
Problem Statement #
Given a number array to represent different coin denominations and a total
amount ‘T’, we need to find all the different ways to make a change for ‘T’
with the given coin denominations. We can assume an infinite supply of coins,
therefore, each coin can be chosen multiple times.
"""

from types import SimpleNamespace
from collections import defaultdict


def coin_change_rec(denominations: list, amount: int) -> list:
    result: list = []
    count: list = []

    def helper(slate: list, idx: int, cur_max_amount: int, amount: int):
        if amount == cur_max_amount:
            result.append(list(slate))
            return
        if idx >= len(denominations) or cur_max_amount > amount:
            return

        if denominations[idx] < amount:
            count.append(idx)
            slate.append(denominations[idx])
            helper(slate, idx, cur_max_amount + denominations[idx], amount)
            slate.pop()
        helper(slate, idx + 1, cur_max_amount, amount)

    helper([], 0, 0, amount)
    print(result)
    print(count)
    print(len(count))
    return len(result)


# ToDo: To Complete
def coin_change_memo(denominations: list, amount: int) -> list:
    result: list = []
    count: list = []

    def helper(slate: list, idx: int, cur_max_amount: int, amount: int):
        if amount == cur_max_amount:
            result.append(list(slate))
            return
        if idx >= len(denominations) or cur_max_amount > amount:
            return

        if denominations[idx] < amount:
            slate.append(denominations[idx])
            helper(slate, idx, cur_max_amount + denominations[idx], amount)
            slate.pop()
        helper(slate, idx + 1, cur_max_amount, amount)

    helper([], 0, 0, amount)
    print(result)
    return len(result)


def coin_change_dp(denominations: list, amount: int) -> list:
    table: List[List[int]] = [[0 for x in range(amount + 1)]
                              for y in range(len(denominations))]

    for col in range(len(table[0])):
        table[0][col] = 1
    for row in range(len(table)):
        table[row][0] = 1

    for row in range(1, len(table)):
        for col in range(1, len(table[row])):
            if col >= denominations[row]:
                table[row][col] = (table[row - 1][col] +
                                   table[row][col - denominations[row]])
            else:
                table[row][col] = table[row - 1][col]

    print(table)
    return table[-1][-1]


print(coin_change_dp([1, 2, 3], 5))
