"""
Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in
a way that will maximize the profit. We are also given the price of every
piece of length ‘i’ where ‘1 <= i <= n’.

Example:
    Lengths: [1, 2, 3, 4, 5]
    Prices: [2, 6, 7, 10, 13]
    Rod Length: 5

Let’s try different combinations of cutting the rod:

Five pieces of length 1 => 10 price
Two pieces of length 2 and one piece of length 1 => 14 price
One piece of length 3 and two pieces of length 1 => 11 price
One piece of length 3 and one piece of length 2 => 13 price
One piece of length 4 and one piece of length 1 => 12 price
One piece of length 5 => 13 price

This shows that we get the maximum price (14) by cutting the rod into
two pieces of length ‘2’ and one piece of length ‘1’.
"""

from types import SimpleNamespace
from collections import defaultdict
from typing import DefaultDict, List


def rod_cutting_rec(lengths: list, prices: list, rod_length: int):
    results: list = []
    price = SimpleNamespace(max=0)

    def helper(slate: list, idx: int, rod_length: int, sold_length: int, cur_profit: int):
        if cur_profit > price.max and sold_length <= rod_length:
            price.max = cur_profit
            results.append(list(slate))

        if idx >= len(lengths) or sold_length >= rod_length:
            return

        slate.append(lengths[idx])
        helper(slate, idx, rod_length, sold_length + lengths[idx],
               cur_profit + prices[idx])
        slate.pop()
        helper(slate, idx + 1, rod_length, sold_length, cur_profit)

    helper([], 0, rod_length, 0, 0)
    print(results)
    return price.max


def rod_cutting_memo(lengths: list, prices: list, rod_length: int):
    results: list = []
    price = SimpleNamespace(max=0)
    memo: DefaultDict = defaultdict(int)

    def helper(slate: list, idx: int, rod_length: int, sold_length: int, cur_profit: int):
        if cur_profit > price.max and sold_length <= rod_length:
            price.max = cur_profit
            results.append(list(slate))
            memo[sold_length] = price.max

        if idx >= len(lengths) or sold_length >= rod_length:
            return

        if sold_length not in memo:
            slate.append(lengths[idx])
            helper(slate, idx, rod_length, sold_length + lengths[idx],
                   cur_profit + prices[idx])
            slate.pop()
        helper(slate, idx + 1, rod_length, sold_length, cur_profit)

    helper([], 0, rod_length, 0, 0)
    print(results)
    return price.max


def rod_cutting_dp(lengths: list, prices: list, rod_lengths: int):
    table: list = [[0 for x in range(rod_lengths + 1)]
                   for y in range(len(lengths))]
    sell_rod_lengths: list = []

    for col in range(len(table[0])):
        if lengths[0] <= col:
            table[0][col] = prices[0] * (col // lengths[0])

    for row in range(1, len(table)):
        for col in range(1, len(table[row])):
            table[row][col] = max(table[row - 1][col],
                                  prices[row] + table[row][col - lengths[row]]
                                  if lengths[row] <= col else 0)
    print(find_selected_length(table, lengths, prices))
    return table[-1][-1]


def find_selected_length(table: List[List[int]], lengths: list, prices: list) -> list:
    row: int = len(table) - 1
    col: int = len(table[0]) - 1
    selected_rods_len: list = []
    while row > 0 and col >= 0:
        if table[row - 1][col] != table[row][col]:
            selected_rods_len.append((lengths[row], prices[row]))
            col -= lengths[row]
        else:
            row -= 1
    if row == 0:
        selected_rods_len.append((lengths[row], prices[row]))

    return selected_rods_len


print(rod_cutting_dp([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
