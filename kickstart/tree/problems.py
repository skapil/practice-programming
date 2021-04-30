from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from typing import Deque, List, Optional


@dataclass
class Node:
    data: int
    left: Optional[Node] = None
    right: Optional[Node] = None


@dataclass
class BinaryTree:
    root: Node

    def in_order(root: Node):
        if root:
            in_order(root.left)
            print(root.data)
            in_order(root.right)

    def pre_order(root: Node):
        if root:
            print(root.data)
            pre_order(root.left)
            pre_order(root.right)

    def post_order(root: Node):
        if root:
            post_order(root.left)
            post_order(root.right)
            print(root.data)


def binary_tree_treversal_bfs(root: Node):
    if not root:
        return []

    result: List[Node] = []
    queue: Deque = deque()
    nodes_count: int = 0

    queue.append(root)
    while queue:
        level_size: int = len(queue)
        current_level: list = []
        for idx in range(level_size):
            node = queue.popleft()
            current_level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result


def reverse_level_order_bfs(root: Node):
    if not root:
        return []

    result: Deque = deque()
    queue: Deque = deque()
    queue.append(root)

    while queue:
        level_size: int = len(queue)
        level_nodes: list = []
        for idx in range(level_size):
            node: Node = queue.popleft()
            level_nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.appendleft(level_nodes)
    return list(result)


def level_order_traversal_zigzag(root: Node):
    if not root:
        return []

    queue: Deque = deque()
    result: list = []
    is_reverse: bool = False

    queue.append(root)
    while queue:
        level_size: int = len(queue)
        level_nodes: Deque = deque()
        for idx in range(level_size):
            node: Node = queue.popleft()
            if is_reverse:
                level_nodes.appendleft(node.data)
            else:
                level_nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        is_reverse = False if is_reverse else True
        result.append(level_nodes)
    return result


def average_of_level_bfs(root: Node):
    if not root:
        return []

    result: list = []
    queue: Deque = deque()
    queue.append(root)
    while queue:
        level_size: int = len(queue)
        level_sum, level_count = 0, 0
        for idx in range(level_size):
            node: Node = queue.popleft()
            level_sum += node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / level_size)
    return result


def main():
    root = Node(12)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(9)
    root.right.left = Node(10)
    root.right.right = Node(5)
    print("Level order traversal: " + str(binary_tree_treversal_bfs(root)))
    print("Level order traversal: " + str(reverse_level_order_bfs(root)))
    print("Level order traversal: " + str(level_order_traversal_zigzag(root)))
    print("Level order traversal: " + str(average_of_level_bfs(root)))


main()
