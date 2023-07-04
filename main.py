# -*- coding: utf-8 -*-
"""Main file"""
from grid import Grid
from shortest_path_tower_bfs import BFS


def main():
    """Main function"""
    filename = "grid.txt"
    grid = Grid(filename)
    bfs = BFS(grid)
    path = bfs.find_path()

    if path is None:
        print("No path found.")
    else:
        print("Found a path with cost: ", path[1])
        for p in path[0]:
            print(p)


if __name__ == "__main__":
    main()