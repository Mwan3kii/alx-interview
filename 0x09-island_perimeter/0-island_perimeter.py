#!/usr/bin/python3
"""Defines function to create island perimeter"""
def island_perimeter(grid):
    """Returns perimeter of island grid"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Check all four sides
                # Top side
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Bottom side
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Left side
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Right side
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter