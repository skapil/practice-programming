from typing import List, DefaultDict
from collections import deque, defaultdict
from heapq import *


def build_graph(edges: int):
    for first, second in input:
        adj_list[first].append(second)


def using_bfs(source: int):
    queue: Deque = deque()
    queue.append(source)
    visited.add(source)
    while queue:
        edge: int = queue.popleft()
        connected_nodes: list = adj_list[edge]
        for neighbor in connected_nodes:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return visited


def using_dfs(source: int):
    visited.add(source)
    for neighbour in adj_list[source]:
        if neighbour not in visited:
            helper(neighbour)


if __name__ == '__main__':
    input = [[0, 1], [1, 2], [3, 4]]
    edges: int = 5
    adj_list: DefaultDict = defaultdict(list)
    build_graph(edges)

    visited: set = set()
    components: int = 0
    print(adj_list)
    for source in range(edges):
        if source not in visited:
            print(source)
            using_bfs(source)
            print(visited)
            using_dfs(source)
            print(visited)
            components += 1
    print(components)
