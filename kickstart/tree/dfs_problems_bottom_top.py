from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from types import SimpleNamespace
import math


@dataclass
class Node:
    data: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def binary_tree_diameter(root: Node):
    if not root.left and not root.right:
        return 0

    height: int = 0
    if root.left:
        left_height: int = binary_tree_diameter(root.left)
        height = left_height + 1
    if root.right:
        right_height: int = binary_tree_diameter(root.right)
        height = right_height + 1
    return height


def count_univalue_subtree(root: Node):
    unival = SimpleNamespace(value=0)

    def helper(root: Node):
        if not root.left and not root.right:
            unival.value += 1
            return True

        is_unival: bool = True
        if root.left:
            is_left_unival = helper(root.left)
            if not is_left_unival or root.data != root.left.data:
                is_unival = False
        if root.right:
            is_right_unival = helper(root.right)
            if not is_right_unival or root.data != root.right.data:
                is_unival = False
        if is_unival:
            unival.value += 1
        return is_unival

    helper(root)
    print(unival)


def lowest_common_ancestor(root: Node, first_node: int, second_node: int):
    result = SimpleNamespace(lca=math.inf)

    def helper(root: Node, first_node: int, second_node: int):
        pfound, qfound = False, False
        if root.data == first_node:
            pfound = True
        if root.data == second_node:
            qfound = True

        if not root.left and not root.right:
            return pfound, qfound

        if root.left:
            pf, qf = helper(root.left, first_node, second_node)
            pfound = pfound or pf
            qfound = qfound or qf
        if root.right:
            pf, qf = helper(root.right, first_node, second_node)
            pfound = pfound or pf
            qfound = qfound or qf
        if pfound and qfound and math.isinf(result.lca):
            result.lca = root.data
        return pfound, qfound

    helper(root, first_node, second_node)
    print(result)


def is_valid_binary_tree(root: Node):
    if not root.left and not root.right:
        return True

    is_left_binary_tree = True
    if root.left:
        is_left_binary_tree = is_valid_binary_tree(root.left)
        if not is_left_binary_tree or root.data < root.left.data:
            is_left_binary_tree = False
    if root.right:
        is_right_binary_tree = is_valid_binary_tree(root.right)
        if not is_right_binary_tree or root.data > root.right.data:
            is_left_binary_tree = False
    return is_left_binary_tree


root: Node = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
print(f"Height of the Tree: {binary_tree_diameter(root)}")

root = Node(5)
root.left = Node(1)
root.left.right = Node(5)
root.left.left = Node(5)
root.right = Node(5)
root.right.right = Node(5)
count_univalue_subtree(root)

root = Node(3)
root.left = Node(5)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right = Node(1)
root.right.right = Node(8)
root.right.left = Node(0)
lowest_common_ancestor(root, 5, 1)
lowest_common_ancestor(root, 5, 4)

root = Node(2)
root.left = Node(1)
root.right = Node(3)
print(f"Is valid binary tree: {is_valid_binary_tree(root)}")

root = Node(5)
root.left = Node(1)
root.right = Node(4)
root.right.right = Node(6)
root.right.left = Node(3)
print(f"Is valid binary tree: {is_valid_binary_tree(root)}")