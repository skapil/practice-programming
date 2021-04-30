"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import Deque, List


def get_neighbours(row: int, col: int):
    result: list = []
    if row - 1 >= 0:
        result.append([row - 1, col])
    if col - 1 >= 0:
        result.append([row, col - 1])
    if row + 1 < len(grid):
        result.append([row + 1, col])
    if col + 1 < len(grid[row]):
        result.append([row, col + 1])
    return result


def bfs(row: int, col: int):
    queue: Deque = deque()
    queue.append((row, col))
    grid[row][col] = 0

    while queue:
        row, col = queue.popleft()
        for row, col in get_neighbours(row, col):
            if grid[row][col]:
                queue.append((row, col))
                grid[row][col] = 0


def dfs(row: int, col: int):
    grid[row][col] = 0

    for row, col in get_neighbours(row, col):
        if grid[row][col]:
            dfs(row, col)


def find_iseland_numbers_bfs():
    islands: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                bfs(row, col)
                islands += 1
    return islands


def find_iseland_numbers_dfs():
    islands: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                dfs(row, col)
                islands += 1
    return islands


if __name__ == '__main__':
    grid: List[List[int]] = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    # print(find_iseland_numbers_bfs())
    print(find_iseland_numbers_dfs())

    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    # print(find_iseland_numbers_bfs())
    print(find_iseland_numbers_dfs())
