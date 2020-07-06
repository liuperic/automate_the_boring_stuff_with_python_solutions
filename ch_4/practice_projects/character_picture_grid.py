#!/usr/bin/env python3

def print_picture_grid(grid):
    row_length = len(grid[0])
    column_length = len(grid)

    for row in range(row_length):
        for column in range(column_length):
            print(grid[column][row], end=' ') 
        print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print_picture_grid(grid)
