import pprint
from collections import defaultdict
from typing import DefaultDict
from types import SimpleNamespace


def length_of_longest_subsequence(arr: list):
    result: list = []
    memo: DefaultDict = defaultdict(list)
    max_length: SimpleNamespace = SimpleNamespace(cur_max_length=0)

    def helper(slate: list, idx: int, is_peak_found: bool):
        if len(slate) >= 3:
            if not is_peak_found and slate[-3] < slate[-2] > slate[-1]:
                is_peak_found = True
            elif is_peak_found:
                if (slate[-3] < slate[-2] > slate[-1] or
                    slate[-1] > slate[-2] or
                        slate[-1] > slate[-3]):
                    return

        if idx >= len(arr):
            memo[idx].append(slate)
            print(slate)
            if len(slate) > max_length.cur_max_length:
                result.pop() if result else None
                result.append(list(slate))
                max_length.cur_max_length = len(slate)
            return
        if len(slate) == 1 and slate[0] > arr[idx]:
            return

        if idx not in memo:
            slate.append(arr[idx])
            helper(slate, idx + 1, is_peak_found)
            slate.pop()
            helper(slate, idx + 1, is_peak_found)

    helper([], 0, False)
    pprint.pprint(result)


if __name__ == '__main__':
    arr: list = [1, 11, 2, 10, 4, 5, 2, 1]
    length_of_longest_subsequence(arr)
