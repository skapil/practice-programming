"""
Given the weights and profits of ‘N’ items, we are asked to put these items
in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit
from the items in the knapsack.
we are allowed to use an unlimited quantity of an item.

Let’s take the example of Merry, who wants to carry some fruits in the
knapsack to get maximum profit. Here are the weights and profits of the fruits:
    Items: { Apple, Orange, Melon }
    Weights: { 1, 2, 3 }
    Profits: { 15, 20, 50 }
    Knapsack capacity: 5

Let’s try to put different combinations of fruits in the knapsack,
such that their total weight is not more than 5.

5 Apples (total weight 5) => 75 profit
1 Apple + 2 Oranges (total weight 5) => 55 profit
2 Apples + 1 Melon (total weight 5) => 80 profit
1 Orange + 1 Melon (total weight 5) => 70 profit

This shows that 2 apples + 1 melon is the best combination,
as it gives us the maximum profit and the total weight does not exceed the
capacity.
"""
from typing import List, DefaultDict
from types import SimpleNamespace
from collections import defaultdict
import pprint


def solve_knapsack_rec(profits: list, weights: list, capacity: int):
    if len(profits) != len(weights):
        raise ValueException("Profits and weights lengths should be same")
    result: List[List[int]] = []
    profit = SimpleNamespace(max=0)

    def helper(slate: list, idx: int, capacity: int, cur_max_profit: int, cur_weight: int):
        if cur_max_profit > profit.max and cur_weight == capacity:
            profit.max = cur_max_profit
            result.append(list(slate))

        if idx >= len(weights) or cur_weight >= capacity:
            return

        if weights[idx] < capacity:
            slate.append((weights[idx], profits[idx]))
            helper(slate, idx, capacity, cur_max_profit + profits[idx],
                   cur_weight + weights[idx])
            slate.pop()
        helper(slate, idx + 1, capacity, cur_max_profit, cur_weight)

    helper([], 0, capacity, 0, 0)
    print(result)
    return profit.max


def solve_knapsack_memo(profits: list, weights: list, capacity: int):
    if len(profits) != len(weights):
        raise ValueException("Profits and weights lengths should be same")
    result: List[List[int]] = []
    profit = SimpleNamespace(max=0)
    memo: DefaultDict = defaultdict(int)

    def helper(slate: list, idx: int, capacity: int, cur_max_profit: int, cur_weight: int):
        if cur_max_profit > profit.max and cur_weight == capacity:
            profit.max = cur_max_profit
            result.append(list(slate))
            memo[cur_weight] = cur_max_profit

        if idx >= len(weights) or cur_weight >= capacity:
            return

        if weights[idx] not in memo and weights[idx] < capacity:
            slate.append((weights[idx], profits[idx]))
            helper(slate, idx, capacity, cur_max_profit + profits[idx],
                   cur_weight + weights[idx])
            slate.pop()
        helper(slate, idx + 1, capacity, cur_max_profit, cur_weight)

    helper([], 0, capacity, 0, 0)
    print(result)
    return profit.max


def solve_knapsack_dp(profits: list, weights: list, capacity: int) -> int:
    table: List[List[int]] = [[0 for x in range(capacity + 1)] for y in range(len(weights))]

    for col in range(1, len(table[0])):
        if col >= weights[0] and weights[0] <= capacity:
            table[0][col] = (col // weights[0]) * profits[0]

    weights_used: set = set()
    for row in range(1, len(table)):
        for col in range(1, len(table[row])):
            exclude_current_weight: int = table[row - 1][col]
            include_current_weight: int = (profits[row] + table[row][col - weights[row]]
                                           if weights[row] <= col else 0)

            if include_current_weight > exclude_current_weight:
                weights_used.add(weights[row])
                table[row][col] = include_current_weight
            else:
                table[row][col] = exclude_current_weight

    pprint.pprint(table)
    print(weights_used)
    return table[-1][-1]


print(solve_knapsack_dp([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(solve_knapsack_dp([15, 50, 60, 90], [1, 3, 4, 5], 6))
