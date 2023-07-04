# -*- coding: utf-8 -*-
"""File to run the shortest path tower problem with A* algorithm implementation"""


def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


# A* algorithm
def a_star(grid, start, goal):
    """A* algorithm implementation"""
    def heuristic(a, b):
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    # Function to find the cell with the lowest f value in the open list
    def find_lowest_f_cell(open_list, score):
        lowest_f = float("inf")
        lowest_f_cell = None
        for cell in open_list:
            if score[cell] < lowest_f:
                lowest_f = score[cell]
                lowest_f_cell = cell
        return lowest_f_cell

    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    open_list = [start]
    paths_and_distances = {start: (None, 0)}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        current = find_lowest_f_cell(open_list, f_score)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                (previous, current_cost) = paths_and_distances[current]
                current = previous
            path.reverse()
            return path, current_cost

        open_list.remove(current)

        for (i, j) in neighbors:
            next_neighbor = (current[0] + i, current[1] + j)
            # check if the neighbor cell is valid
            if 0 <= next_neighbor[0] < len(grid) and 0 <= next_neighbor[1] < len(grid[0]):
                if grid[next_neighbor[0]][next_neighbor[1]] != '1':
                    new_cost = paths_and_distances[current][1] + 1
                    if next_neighbor not in paths_and_distances or new_cost < paths_and_distances[next_neighbor][1]:
                        paths_and_distances[next_neighbor] = (current, new_cost)
                        f_score[next_neighbor] = new_cost + heuristic(goal, next_neighbor)
                        if next_neighbor not in open_list:
                            open_list.append(next_neighbor)
    return None, None


# Main function
def main():
    filename = "grid.txt"
    grid = read_grid_from_file(filename)
    start, goal = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)

    if start is None or goal is None:
        print("Start or goal not found in the grid.")
        return

    path, cost = a_star(grid, start, goal)
    if path is None:
        print("No path found.")
    else:
        print("Found a path with cost: ", cost)
        for p in path:
            print(p)


if __name__ == "__main__":
    main()
