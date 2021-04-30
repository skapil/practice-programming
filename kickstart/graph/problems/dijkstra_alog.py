from queue import PriorityQueue
from typing import List


def calculate_distances(graph: List[List[int]], starting_vertex: int):
    queue: PriorityQueue = PriorityQueue()
    distance: Deque = {vertex: float("inf") for vertex in example_graph}
    distance[starting_vertex] = 0
    queue.put((0, starting_vertex))

    while not queue.empty():
        cur_dist, cur_vertex = queue.get()
        if cur_dist > distance[cur_vertex]:
            continue
        for neighbour, weight in graph[cur_vertex].items():
            neighbour_distance = weight + cur_dist
            if neighbour_distance < distance[neighbour]:
                distance[neighbour] = neighbour_distance
                queue.put((neighbour_distance, neighbour))

    print(distance)


if __name__ == "__main__":
    example_graph = {
        "U": {"V": 2, "W": 5, "X": 1},
        "V": {"U": 2, "X": 2, "W": 3},
        "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
        "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
        "Y": {"X": 1, "W": 1, "Z": 1},
        "Z": {"W": 5, "Y": 1},
    }
    print(calculate_distances(example_graph, "X"))
    # => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}