from types import SimpleNamespace
from collections import defaultdict
from typing import DefaultDict


def solve_knapsack(profits: list, weights: list, capacity: int):
    result = SimpleNamespace(max_profit=0, capacity=capacity)

    def helper(idx: int, cur_weight: int, cur_profit: int):
        if cur_weight > result.capacity:
            return
        result.max_profit = max(result.max_profit, cur_profit)
        if idx >= len(weights):
            return
        helper(idx + 1, cur_weight, cur_profit)
        cur_weight += weights[idx]
        cur_profit += profits[idx]
        helper(idx + 1, cur_weight, cur_profit)

    helper(0, 0, 0)
    print(result)


def solve_knapsack_bu(profits: list, weights: list, capacity: int):
    def helper(capacity: int, idx: int, slate: list):
        if capacity <= 0 or idx >= len(weights):
            return 0

        first_profit: int = 0
        if weights[idx] <= capacity:
            slate.append([profits[idx], weights[idx]])
            first_profit = profits[idx] + helper(
                capacity - weights[idx], idx + 1, slate
            )
            slate.pop()

        second_profit = helper(capacity, idx + 1, slate)
        return max(first_profit, second_profit)

    print(helper(capacity, 0, []))


def solve_knapsack_memo(profits: list, weights: list, capacity: int):
    memo: DefaultDict = defaultdict(int)

    def helper(capacity: int, idx: int):
        if capacity <= 0 or idx >= len(weights):
            return 0

        if (idx, capacity) in memo:
            return memo[(idx, capacity)]

        first_profit: int = 0
        if capacity >= weights[idx]:
            first_profit = profits[idx] + helper(capacity - weights[idx], idx + 1)

        second_profit = helper(capacity, idx + 1)
        memo[(idx, capacity)] = max(first_profit, second_profit)
        return memo[(idx, capacity)]

    print(helper(capacity, 0))
    print(memo)


def is_equal_subset(arr: list):
    sum_arr: int = sum(arr)
    if sum_arr & 1:
        return False
    subset_sum: int = sum_arr // 2

    result: list = []

    def helper(idx: int, slate: list, cur_sum: int, subset_sum: int):
        if cur_sum == subset_sum:
            result.append(slate.copy())
            return
        if idx >= len(arr):
            return

        slate.append(arr[idx])
        helper(idx + 1, slate, cur_sum + arr[idx], subset_sum)
        slate.pop()
        helper(idx + 1, slate, cur_sum, subset_sum)

    helper(0, [], 0, subset_sum)
    print(result)


def is_equal_subset_bu(arr: list):
    sum_arr: int = sum(arr)
    if sum_arr & 1:
        print("False")
        return False
    subset_sum: int = sum_arr // 2

    def helper(idx: int, subset_sum: int):
        if subset_sum == 0:
            return True
        if idx >= len(arr):
            return False

        first_result = helper(idx + 1, subset_sum - arr[idx])
        second_result = helper(idx + 1, subset_sum)
        return first_result or second_result

    print(helper(0, subset_sum))


def can_partitions(arr: list, target: int):
    result: list = []

    def helper(idx: int, slate: list, cur_sum: int, target: int):
        if not result and cur_sum == target:
            result.append(slate.copy())
        if idx >= len(arr):
            return

        slate.append(arr[idx])
        helper(idx + 1, slate, cur_sum + arr[idx], target)
        slate.pop()
        helper(idx + 1, slate, cur_sum + arr[idx], target)

    helper(0, [], 0, target)
    print(result)


def can_partitions_bu(arr: list, target: int):
    result: list = []

    def helper(idx: int, slate: list, target: int):
        if target == 0:
            result.append(slate.copy())
            return True
        if idx >= len(arr):
            return False

        include: bool = False
        if target >= arr[idx]:
            slate.append(arr[idx])
            include = helper(idx + 1, slate, target - arr[idx])
            slate.pop()
            if include:
                return True
        exclude: bool = helper(idx + 1, slate, target)
        return include or exclude

    print(helper(0, [], target))
    print(result)


def can_partitions_memo(arr: list, target: int):
    result: list = []
    memo: DefaultDict = defaultdict(int)

    def helper(idx: int, slate: list, target: int):
        if target == 0:
            result.append(slate.copy())
            return True
        if idx >= len(arr):
            return False
        if (idx, target) in memo:
            return memo[(idx, target)]

        include: bool = False
        if target >= arr[idx]:
            slate.append(arr[idx])
            include = helper(idx + 1, slate, target - arr[idx])
            slate.pop()
            if include:
                return True
        exclude: bool = helper(idx + 1, slate, target)
        memo[(idx, target)] = include or exclude
        return memo[(idx, target)]

    helper(0, [], target)
    print(result)
    print(memo)


def test_can_partition():
    can_partitions_memo([1, 2, 3, 7], 6)
    can_partitions_memo([1, 2, 7, 1, 5], 10)
    can_partitions_memo([1, 3, 4, 8], 6)


def test_is_equal_subset():
    is_equal_subset_bu([1, 2, 3, 4])
    is_equal_subset_bu([1, 1, 3, 4, 7])
    is_equal_subset_bu([2, 3, 4, 6])


def test_solve_knapsack():
    solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)
    solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)


def test_solve_knapsack_memo():
    solve_knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 7)
    solve_knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 6)


if __name__ == "__main__":
    test_can_partition()