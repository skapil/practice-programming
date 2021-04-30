from typing import List, DefaultDict
from collections import defaultdict
from queue import PriorityQueue


def build_graph():
    graph: DefaultDict = defaultdict(list)
    for source, dest, time_taken in times:
        graph[source].append((dest, time_taken))

    return graph


def get_time_all_signals(time_taken: int, source: int, nodes: int):
    network_timings: DefaultDict = defaultdict(int)
    queue: PriorityQueue = PriorityQueue()
    last_dist: int = float("inf")
    last_captured: int = float("inf")
    queue.put((time_taken, source))

    while not queue.empty():
        network_time, network = queue.get()
        if network not in network_timings:
            network_timings[network] = network_time
            last_captured += 1
            last_dist = network
            for neighbour, time_taken in graph[network]:
                if neighbour not in network_timings:
                    queue.put((time_taken + network_time, neighbour))

    print(network_timings)
    if last_captured < nodes:
        return -1
    return last_dist


def total_reach_time_networks(starting_vertex: int, nodes: int):
    distances: DefaultDict = defaultdict(int)
    distances[starting_vertex] = 0
    queue = PriorityQueue()
    queue.put((0, starting_vertex))

    while not queue.empty():
        cur_dist, cur_vertex = queue.get()
        if cur_dist > distances[cur_vertex]:
            continue
        for neighbour, weight in graph[cur_vertex]:
            distance: int = weight + cur_dist
            if neighbour not in distances or distance < distances[neighbour]:
                distances[neighbour] = distance
                queue.put((distance, neighbour))

    print(distances)


if __name__ == "__main__":
    times: List[List[int]] = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    nodes, source = 4, 2
    graph: DefaultDict = build_graph()

    print(get_time_all_signals(0, source, nodes))
    print(total_reach_time_networks(source, nodes))
