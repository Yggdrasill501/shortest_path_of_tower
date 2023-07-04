from queue import Queue

class BFS:
    def __init__(self, grid):
        self.grid = grid
        self.queue = Queue()
        self.paths = {grid.start: None}

    def find_path(self):
        self.queue.enqueue(self.grid.start)
        while not self.queue.is_empty():
            current = self.queue.dequeue()
            if current == self.grid.goal:
                return self.reconstruct_path(current)

            for next in self.grid.get_neighbors(current):
                if next not in self.paths:
                    self.paths[next] = current
                    self.queue.enqueue(next)

        return None

    def reconstruct_path(self, current):
        path = []
        while current is not None:
            path.append(current)
            current = self.paths[current]
        path.reverse()
        return path, len(path) - 1