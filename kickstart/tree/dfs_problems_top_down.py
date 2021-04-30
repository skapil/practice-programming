from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from types import SimpleNamespace


@dataclass
class Node:
    data: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def print_all_paths(root: Node):
    result: list = []

    def helper(root: Node, slate: list):
        slate.append(root.data)

        if not root.left and not root.right:
            result.append(slate.copy())
            # slate.pop()
            # return

        if root.left:
            helper(root.left, slate)
        if root.right:
            helper(root.right, slate)

        slate.pop()

    helper(root, [])
    print(result)


def path_sum(root: Node, given_sum: int):
    result = SimpleNamespace(given_sum=given_sum)

    def helper(root: Node, cur_sum: int):
        cur_sum += root.data
        if not root.left and not root.right:
            if cur_sum == result.given_sum:
                result.is_target = True

        if root.left:
            helper(root.left, cur_sum)
        if root.right:
            helper(root.right, cur_sum)

    helper(root, 0)
    print(result)


def path_sum_II(root: Node, target_sum: int):
    result: list = []

    def helper(root: Node, target_sum: int, cur_sum: int, slate: int):
        cur_sum += root.data
        slate.append(root.data)

        if not root.left and not root.right:
            if cur_sum == target_sum:
                result.append(slate.copy())

        if root.left:
            helper(root.left, target_sum, cur_sum, slate)
        if root.right:
            helper(root.right, target_sum, cur_sum, slate)

        slate.pop()

    helper(root, target_sum, 0, [])
    print(result)


def get_longest_consecutive_sequence(source: Node):
    longest = SimpleNamespace(nodes=0)

    def helper(source: Node, parent: Node, cur_max: list):
        if parent and source.data == parent.data + 1:
            cur_max += 1
        else:
            longest.nodes = max(longest.nodes, cur_max)
            cur_max = 1

        if not source.left and not source.right:
            longest.nodes = max(longest.nodes, cur_max)
            cur_max = 1
        if source.left:
            helper(source.left, source, cur_max)
        if source.right:
            helper(source.right, source, cur_max)

    helper(source, None, 0)
    print(longest)


def get_path_sum_III(source: Node, target: int):
    result: list = []

    def helper(source: Node, target: int, slate: list):
        slate.append(source.data)
        prefix, cur_sum = [], 0
        for value in reversed(slate):
            prefix.append(value)
            cur_sum += value
            if cur_sum == target:
                result.append(prefix.copy())
        if source.left:
            helper(source.left, target, slate)
        if source.right:
            helper(source.right, target, slate)
        slate.pop()

    helper(source, 8, [])
    print(f"All path sum: {result}")


def k_ary_tree_edge_height(root: Node):
    if not root:
        return None
    result = SimpleNameSpace(height=0)

    # For edges height, we need height until parents
    def helper(root: Node, parent_height: int):
        cur_height = parent_height + 1
        result.height = max(result.height, cur_height)

        for child in Node.childrens:
            k_ary_tree_height(child, cur_height)

    helper(root, -1)
    print(height)


if __name__ == "__main__":
    root: Node = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    root.right.left = Node(6)
    print_all_paths(root)

    root = Node(5)
    root.left = Node(4)
    root.left.left = Node(11)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    root.right = Node(8)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.right.right.right = Node(1)
    root.right.right.left = Node(5)
    path_sum(root, 22)
    path_sum_II(root, 22)

    root = Node(1)
    root.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(4)
    root.right.right.right = Node(5)
    get_longest_consecutive_sequence(root)

    root = Node(2)
    root.right = Node(3)
    root.right.left = Node(2)
    root.right.left.left = Node(1)
    get_longest_consecutive_sequence(root)

    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right = Node(2)
    root.left.right.right = Node(1)
    root.right = Node(-3)
    root.right.right = Node(11)
    get_path_sum_III(root, 8)
