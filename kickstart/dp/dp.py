from collections import defaultdict
from typing import DefaultDict, List


def ways_to_climb_staircase(stairs: int):
    table: list = [0] * (stairs + 1)
    if stairs <= 2:
        return stairs
    table[0], table[1], table[2] = 0, 1, 2
    for idx in range(3, len(table)):
        table[idx] = table[idx - 1] + table[idx - 2]

    print(table)
    print(table[stairs])
    return table[stairs]


def solve_knapsack(profits: list, weights: list, capacity: int, idx: int):
    if capacity <= 0 or idx >= len(profits):
        return 0

    profit1: int = 0
    if weights[idx] <= capacity:
        profit1 = (profits[idx] +
                   solve_knapsack(profits, weights, capacity - weights[idx], idx + 1))

    profit2 = solve_knapsack(profits, weights, capacity, idx + 1)
    return max(profit1, profit2)


def ways_to_make_score(final_score: int):
    scores: DefaultDict = defaultdict(int)

    def helper(final_score: int, idx: int):
        if final_score < 0 or final_score == 1:
            return scores[1]
        if final_score == 0:
            scores[0] = 1
            return scores[0]

        scores[idx] = (helper(final_score - 2, idx + 1) +
                       helper(final_score - 3, idx + 1) +
                       helper(final_score - 6, idx + 1))
        return scores[idx]

    helper(final_score, 0)


def ways_to_make_score_dp(final_score: int, possible: list) -> int:
    scores: list = [0] * (final_score + 1)
    scores[0], scores[1] = 1, 0
    for idx in range(2, final_score + 1):
        for score in possible:
            if idx - score >= 0:
                scores[idx] += scores[idx - score]

    return scores[final_score]


def subset(word: str):
    result: list = []

    def helper(word: str, slate: list, idx: int):
        if idx >= len(word) or len(slate) >= len(word):
            result.append(''.join(list(slate)))
            return
        helper(word, slate + [word[idx]], idx + 1)
        helper(word, slate, idx + 1)

    helper(word, [], 0)
    print(result)


def unique_path(m: int, n: int):
    table: List[List[int]] = [[1] * n for _ in range(m)]
    for row in range(len(table)):
        for col in range(len(table[row])):
            if row and col:
                table[row][col] = table[row - 1][col] + table[row][col - 1]

    print(table[m - 1][n - 1])


if __name__ == '__main__':
    unique_path(3, 7)
