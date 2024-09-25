#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.
    Args:
    grid (list of list of int): A 2D list representing the grid,
    where 0 represents water and 1 represents land.
    Returns:
    int: The perimeter of the island.
    """
    if not grid:
        return 0
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:  # Up
                    perimeter += 1
                if r == rows - 1 or grid[r+1][c] == 0:  # Down
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # Left
                    perimeter += 1
                if c == cols - 1 or grid[r][c+1] == 0:  # Right
                    perimeter += 1
    return perimeter
