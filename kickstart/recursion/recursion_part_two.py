from types import SimpleNamespace


def solve_knapsack(profits: list, weights: list, capacity: int):
    knapsack = SimpleNamespace(
        capacity=capacity, max_capacity=0, weights=[], max_profit=0
    )

    def helper(idx: int, slate: list, cur_capacity: int, cur_profit: int):
        if cur_capacity == knapsack.capacity:
            knapsack.max_profit = max(knapsack.max_profit, cur_profit)
            knapsack.weights.append(slate.copy())
        if cur_capacity > knapsack.capacity:
            return
        if idx >= len(weights):
            return

        slate.append(weights[idx])
        helper(idx, slate, cur_capacity + weights[idx], cur_profit + profits[idx])
        slate.pop()
        helper(idx + 1, slate, cur_capacity, cur_profit)

    helper(0, [], 0, 0)
    print(knapsack)


def solve_knapsack_bu(profits: list, weights: list, capacity: int):
    def helper(idx: int, slate: list, capacity: int):
        if idx >= len(weights) or capacity <= 0:
            return 0

        include: int = 0
        if weights[idx] <= capacity:
            include = profits[idx] + helper(idx, slate, capacity - weights[idx])

        exclude: int = helper(idx + 1, slate, capacity)
        max_profit: int = max(include, exclude)
        return max_profit

    print(helper(0, [], capacity))


def test_solve_knapsack():
    solve_knapsack_bu([15, 50, 60, 90], [1, 3, 4, 5], 8)
    solve_knapsack_bu([15, 50, 60, 90], [1, 3, 4, 5], 6)


if __name__ == "__main__":
    test_solve_knapsack()