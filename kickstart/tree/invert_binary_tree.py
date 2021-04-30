from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Deque
from collections import deque


@dataclass
class Node:
    data: int
    left: Optiona[Node] = None
    right: Optiona[Node] = None


def inorder(root: Node):
    result: list = []

    def helper(root: Node):
        if root.left:
            helper(root.left)
        result.append(root.data)
        if root.right:
            helper(root.right)

    helper(root)
    print(result)


def invert_binary_tree_dfs(root: Node):
    if not root:
        return None

    reverse_tree: Node = Node(root.data)

    def helper(root: Node, reverse_tree: Node):
        if root.left:
            reverse_tree.right = Node(root.left.data)
            helper(root.left, reverse_tree.right)
        if root.right:
            reverse_tree.left = Node(root.right.data)
            helper(root.right, reverse_tree.left)

    helper(root, reverse_tree)
    inorder(reverse_tree)
    print(reverse_tree)
    print("****************************")


def invert_binary_tree_bfs(root: Node):
    if not root:
        return None

    reverse_bfs_tree: Node = Node(root.data)
    reverse_root: Node = reverse_bfs_tree
    queue: Deque = deque()
    queue.append((reverse_bfs_tree, root))

    while queue:
        level_len: int = len(queue)
        level_nodes: list = []
        for idx in range(level_len):
            reverse_node, node = queue.popleft()
            if node.left:
                reverse_node.right = Node(node.left.data)
                queue.append((reverse_node.right, node.left))
            if node.right:
                reverse_node.left = Node(node.right.data)
                queue.append((reverse_node.left, node.right))

    print(reverse_root)


root: Node = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)
invert_binary_tree_dfs(root)
invert_binary_tree_bfs(root)