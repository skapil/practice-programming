from types import SimpleNamespace


def longest_increasing_subequence_rec(input: list):
    result = SimpleNamespace(lca=[], max_len=0)

    def helper(slate: list, cur: int, prev: int):
        if len(slate) > result.max_len:
            result.max_len = len(slate)
            result.lca = list(slate)

        if cur == len(input):
            return 0

        if prev == -1 or input[cur] > input[prev]:
            helper(slate + [input[cur]], cur + 1, cur)

        helper(slate, cur + 1, prev)

    print(helper([], 0, -1))
    print(result)


def longest_increasing_subsequence_dp(input: list) -> int:
    plow: List[List[int]] = [1 for x in range(len(input))]

    for edge in range(1, len(plow)):
        for roll in range(edge):
            if input[roll] <= input[edge] and plow[roll] >= plow[edge]:
                plow[edge] += 1

    print(plow)
    return plow[-1]


longest_increasing_subsequence_dp([4, 2, 3, 6, 10, 1, 12])
