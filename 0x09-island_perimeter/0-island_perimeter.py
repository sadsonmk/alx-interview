#!/usr/bin/python3
"""This is a module for a function island_perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""

    h = len(grid)
    w = len(grid[0])

    def dfs(row, col):
        """a helper function for the depth first search"""
        if row < 0 or row >= h or col < 0 or col >= w or grid[row][col] == 0:
            return 1
        if grid[row][col] == 1:
            grid[row][col] = 2
            return dfs(row - 1, col) + dfs(row + 1, col) + \
                dfs(row, col - 1) + dfs(row, col + 1)
        return 0
    total = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c]:
                total += dfs(r, c)
    return total
