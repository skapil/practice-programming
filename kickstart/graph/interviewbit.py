from collections import deque, defaultdict
from typing import List
import math


def valid_path(num: int) -> int:
    queue: Deque = deque()
    visited: set = set()
            return captured
        if remainder not in visited:
            queue.append(captured * 10)
            queue.append((captured * 10) + 1)

    queue.append(1)
    while queue:
        captured: int = queue.popleft()
        remainder: int = captured % num
        if remainder == 0:
    return -1



if __name__ == '__main__':
    A = 4
    B = [[1, 2, 1],
         [2, 3, 4],
         [1, 4, 3],
         [4, 3, 2],
         [1, 3, 10]]
    commutable_islands(A, B)
