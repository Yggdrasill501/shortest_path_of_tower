# -*- coding: utf-8 -*-
""" Breadth First Search File"""
from queue import Queue


class BreadthFirstSearch:
    """Breadth First Search Algorithm"""

    def __init__(self, grid):
        """Init"""
        self.grid = grid
        self.queue = Queue()
        self.paths = {grid.start: None}

    def find_path(self):
        """Find path from start to goal"""
        self.queue.enqueue(self.grid.start)

        while not self.queue.is_empty():
            current = self.queue.dequeue()

            if current == self.grid.goal:
                return self.reconstruct_path(current)

            for next_neighbor in self.grid.get_neighbors(current):
                if next_neighbor not in self.paths:
                    self.paths[next_neighbor] = current
                    self.queue.enqueue(next_neighbor)

        return None

    def reconstruct_path(self, current) -> tuple:
        """Reconstruct path from start to goal"""
        path = []

        while current is not None:
            path.append(current)
            current = self.paths[current]

        path.reverse()
        return path, len(path) - 1
