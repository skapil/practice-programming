from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Deque, Optional


@dataclass
class Node:
    data: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def left_tree_value_bfs(root: Node):
    result: Node = None
    queue: Deque = deque()
    queue.append(root)
    left_most: Node = None
    while len(queue) > 0:
        level_len: int = len(queue)
        left_most: Node = None
        for children in range(level_len):
            node: Node = queue.popleft()
            if node.left:
                queue.append(node.left)
                if not left_most:
                    left_most = node.left
                    result = left_most
            if node.right:
                queue.append(node.right)
    print(result)


def is_tree_height_balance(source: Node):
    result = SimpleNamespace(is_balance=True)

    def helper(source: Node):
        if not source.left and not source.right:
            return 0

        left_height, right_height = 0, 0
        if source.left:
            left_height = helper(source.left) + 1
        if source.left:
            right_height = helper(source.right) + 1

        if result.is_balance and abs(left_height - right_height) not in {0, 1}:
            print(f"Tree is unbalance: {root}, {left_height} {right_height}")
            result.is_balance = False

        return max(left_height, right_height)

    helper(source)
    print(result)


# LeetCode Problem: 563
def binary_tree_tilt(root: Node):
    if not root.left and not root.right:
        return 0
    tilt = 0
    if root.left:
        tilt = binary_tree_tilt(root.left)
    if root.right:
        tilt = binary_tree_tilt(root.left)
    tilt += abs(root.left.data - root.right.data)
    return tilt


root: Node = Node(2)
root.left = Node(1)
root.right = Node(3)
left_tree_value_bfs(root)


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)
root.right.left = Node(5)
root.right.left.left = Node(7)
root.right.right = Node(6)
left_tree_value_bfs(root)

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.right = Node(7)
root.right.left = Node(15)
is_tree_height_balance(root)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.right = Node(3)
root.left.left = Node(3)
root.left.left.right = Node(4)
root.left.left.left = Node(4)
is_tree_height_balance(root)

root: Node = Node(1)
root.left = Node(2)
root.right = Node(3)
print(f"Tilt Value of Tree: {binary_tree_tilt(root)}")
