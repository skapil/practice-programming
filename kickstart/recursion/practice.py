def subset(nums: list) -> None:
    result: list = []

    def helper(idx: int, slate: list):
        if idx >= len(nums):
            result.append(list(slate))
        else:
            slate.append(nums[idx])
            helper(idx + 1, slate)
            slate.pop()
            helper(idx + 1, slate)

    helper(0, [])
    print(result)


def equal_subset_partition(nums: list) -> None:
    first: list = set()

    def helper(idx: int, nums_sum: int, slate: set, slate_sum: int):
        if nums_sum == slate_sum:
            first.update(set(slate))
            return True
        if idx >= len(nums):
            return False

        slate.add(idx)
        if helper(idx + 1, nums_sum - nums[idx], slate, slate_sum + nums[idx]):
            return True
        slate.remove(idx)
        if helper(idx + 1, nums_sum, slate, slate_sum):
            return True

        return False

    nums_sum: int = sum(nums)
    helper(0, nums_sum, set(), 0)
    second: list = set(idx for idx in range(len(nums)) if idx not in first)
    print(first, second)


def solve_knapsack(profits: list, weights: list, capacity: int):

    def helper(capacity: int, idx: int):
        if capacity <= 0 or idx >= len(weights):
            return 0

        profit1 = 0
        if weights[idx] <= capacity:
            profit1 = profits[idx] + helper(capacity - weights[idx], idx + 1)
        profit2 = helper(capacity, idx + 1)
        return max(profit1, profit2)

    return helper(capacity, 0)


def can_partition(data: list) -> bool:
    target: int = sum(data)
    if 1 & target:
        return False
    target /= 2
    result: list = []

    def helper(slate: list, idx: int, target: int):
        if sum(slate) == target:
            result.append(list(slate))
            return
        if idx >= len(data):
            return

        helper(slate + [data[idx]], idx + 1, target)
        helper(slate, idx + 1, target)

    helper([], 0, target)
    print(result)
    if result:
        return True
    return False


print("Can partition: " + str(can_partition([1, 2, 3, 4])))
print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
print("Can partition: " + str(can_partition([2, 3, 4, 6])))
