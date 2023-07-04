# -*- coding: utf-8 -*-
"""File to read grid"""


class Grid:
    """Read gird from file and find neighbors of a position."""

    def __init__(self, filename) -> None:
        """Init"""
        with open(filename, 'r') as file:
            self.grid = [list(line.strip()) for line in file]

        self.start, self.goal = None, None
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'S':
                    self.start = (i, j)
                elif self.grid[i][j] == 'E':
                    self.goal = (i, j)

        if self.start is None or self.goal is None:
            raise ValueError("Start or goal not found in the grid.")

    def get_neighbors(self, position) -> list:
        """Get neighbors of a position"""

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = []

        for (i, j) in neighbors:
            next_neighbor = (position[0] + i, position[1] + j)
            if 0 <= next_neighbor[0] < len(self.grid) and 0 <= next_neighbor[1] < len(self.grid[0]):
                if self.grid[next_neighbor[0]][next_neighbor[1]] != '1':
                    result.append(next_neighbor)

        return result
