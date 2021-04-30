from collections import defaultdict, deque
from typing import DefaultDict, Deque, List


def build_graph():
    for src, dest in edges:
        graph[src].append(dest)


def is_cycle_bfs(source: int):
    queue: Deque = deque()
    queue.append(source)
    visited[source] = 1

    while queue:
        vertice: int = queue.popleft()
        vertices: list = graph[vertice]
        for neighbour in vertices:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
                parents[neighbour] = vertice
            else:
                if parents[neighbour] != vertice:
                    return True
    return False


def is_cycle_dfs(source: int) -> bool:
    visited[source] = True

    for neighbour in graph[source]:
        if not visited[neighbour]:
            parents[neighbour] = source
            is_cycle = is_cycle_bfs(source)
            if is_cycle:
                break
        else:
            if parents[neighbour] != source:
                return True
    return False


def using_bfs() -> tuple:
    components: int = 0
    is_cycle: bool = False
    for source in range(5):
        if not visited[source]:
            is_cycle = is_cycle_bfs(source)
            if is_cycle:
                break
            components += 1
    return components, is_cycle


def using_dfs() -> tuple:
    components: int = 0
    is_cycle: bool = False
    print(graph)
    for source in range(5):
        print(visited)
        if not visited[source]:
            is_cycle = is_cycle_bfs(source)
            if is_cycle:
                break
            components += 1

    return components, is_cycle


def is_valid_tree():
    #components, is_cycle = using_bfs()
    components, is_cycle = using_dfs()

    print(components, is_cycle)
    if components > 1 or is_cycle:
        print("Tree is not possible")
    else:
        print("Tree is possible")


if __name__ == '__main__':
    edges: List[List[int]] = [[0, 1], [0, 2], [0, 3], [1, 4]]
    graph: DefaultDict = defaultdict(list)
    nodes: int = 5

    # Buidling the graph
    build_graph()
    visited: list = [None] * nodes
    # Parents will help us to find cyclic graph
    parents: list = [None] * nodes
    is_valid_tree()

    ########### 2nd Test Case ##################
    edges: List[List[int]] = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    graph = defaultdict(list)
    nodes = 5

    # Buidling the graph
    build_graph()
    visited = [None] * nodes
    # Parents will help us to find cyclic graph
    parents = [None] * nodes
    is_valid_tree()
