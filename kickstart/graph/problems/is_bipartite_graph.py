from collections import defaultdict, deque
from typing import DefaultDict, Deque, List


def build_graph():
    for source, dest in input:
        graph[source].append(dest)
        graph[dest].append(source)


def is_bipartite_dfs(source: int):
    visited[source] = True
    for neighbour in graph[source]:
        if not visited[neighbour]:
            parents[neighbour] = source
            parent: int = parents[neighbour]
            colors[neighbour] = 'R' if colors[parent] == 'B' else 'B'
            if is_bipartite_dfs(neighbour):
                return True
        else:
            if parents[neighbour] != source and colors[neighbour] == colors[source]:
                return False
    return True


def is_bipartite_bfs(source: int):
    queue: Deque = deque()

    queue.append(source)
    visited[source] = True

    while queue:
        source = queue.popleft()
        for neighbour in graph[source]:
            if not visited[neighbour]:
                queue.append(neighbour)
                parents[neighbour] = source
                distance[neighbour] = 1 + distance[source]
            else:
                if (neighbour != parents[source] and
                        distance[neighbour] != distance[source]):
                    return False
    return True


def using_bfs():
    is_bipartite: bool = False
    for source in graph:
        is_bipartite = is_bipartite_bfs(source)

    if is_bipartite:
        print("This bipartite graph.")
    else:
        print("This is not bipartite graph.")


def using_dfs():
    is_bipartite: bool = False
    for source in graph:
        is_bipartite = is_bipartite_dfs(source)

    if is_bipartite:
        print("This bipartite graph.")
    else:
        print("This is not bipartite graph.")


if __name__ == '__main__':
    input: [List[List[int]]] = [[1, 3], [0, 2], [1, 3], [0, 2]]

    graph: DefaultDict = defaultdict(list)
    build_graph()

    visited: list = [None] * len(graph)
    parents: list = [None] * len(graph)
    distance: list = [0] * len(graph)
    colors: list = [None] * len(graph)
    colors[0] = 'R'
    using_bfs()

    # using_dfs()
