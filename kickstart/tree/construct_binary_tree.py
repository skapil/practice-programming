from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    data: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def to_bst(arr: list):
    def helper(start: int, end: int):
        if start > end:
            return None
        elif start == end:
            return Node(arr[start])
        else:
            mid = start + ((end - start) // 2)
            root = Node(arr[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root

    print(helper(0, len(arr) - 1))


if __name__ == "__main__":
    arr: list = [-10, -3, 0, 5, 9]
    to_bst(arr)