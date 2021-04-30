from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from types import SimpleNamespace


@dataclass
class Node:
    data: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def find_nodes_with_target(root: Node, target: int):
    result: list = []
    if not root:
        return result

    def helper(root: node, target: int, slate: list):
        slate.append(root.data)

        if not any([node.left, node.right]):
            if target == node.data:
                result.append(slate.copy())
            return

        if node.left:
            helper(root.left, target - node.data, slate)
        if node.right:
            helper(root.right, target - node.data, slate)

        slate.pop()

    helper(root, target, [])
    print(result)
    return result


def diameter_binary_tree(root: Node):
    if not root:
        return 0
    diameter = SimpleNamespace(max_length=0)

    def helper(root: Node):
        if not root:
            return 0

        left_height = helper(root.left)
        right_height = helper(root.right)

        max_diameter = left_height + right_height + 1
        diameter.max_length = max(diameter.max_length, max_diameter)
        return max(left_height, right_height) + 1

    helper(root)
    print(diameter)


def path_with_maximum_sum(root: Node):
    if not root:
        return 0

    path = SimpleNamespace(max_sum=0)

    def helper(root: Node):
        if not root:
            return 0

        left_tree_sum = helper(root.left)
        right_tree_sum = helper(root.right)
        left_tree_sum = max(left_tree_sum, 0)
        right_tree_sum = max(right_tree_sum, 0)
        local_path_sum = left_tree_sum + right_tree_sum + root.data
        path.max_sum = max(local_path_sum, path.max_sum)
        return max(left_tree_sum, right_tree_sum) + root.data

    helper(root)
    print(path)


def univalue_subtree(root: Node):
    if not root:
        return 0
    univalue = SimpleNamespace(subtree=0)

    def helper(root: Node):
        if not root:
            return 0
        if not root.left and not root.right:
            univalue.subtree += 1
            return 1

        left_node = helper(root.left)
        right_node = helper(root.right)
        if root.left and not root.right and root.data == root.left.data:
            univalue.subtree += 1
        elif root.right and not root.left and root.data == root.right.data:
            univalue.subtree += 1
        elif root.data == root.left.data == root.right.data:
            univalue.subtree += 1
        return max(left_node, right_node)

    helper(root)
    print(univalue)


def is_unival_subtree(root: Node):
    if not root:
        return

    unvalue = SimpleNamespace(subtree=0)

    def helper(root: Node):
        if not root.left and not root.right:
            return True

        unival = True
        if root.left:
            left_val = helper(root.left)
            if not left_val or root.data != root.left.data:
                unival = False
        if root.right:
            right_val = helper(root.right)
            if not right_val or root.data != root.right.data:
                unival = False

        if unival:
            unvalue.subtree += 1
        return unival

    helper(root)
    print(unvalue)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    path_with_maximum_sum(root)

    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(9)
    path_with_maximum_sum(root)

    root = Node(-1)
    root.left = Node(-3)
    path_with_maximum_sum(root)

    root = Node(5)
    root.left = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(5)
    root.right = Node(5)
    root.right.right = Node(5)
    univalue_subtree(root)
    is_unival_subtree(root)
    univalue_subtree(root)