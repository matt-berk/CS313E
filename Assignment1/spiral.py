"""
  File: spiral.py
  Description: Creates a spiral out of a 2d list and can calculate the sum of adjacent numbers

  Student Name: Matthew Berk
  Student UT EID: mb67665

  Partner Name: Charles Ruhmann
  Partner UT EID: CJR3946

  Course Name: CS 313E
  Unique Number: 50165
  Date Created: 8/28/24
  Date Last Modified: 8/29/24
"""

import math


def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""

    # ADD YOUR CODE HERE
    # Initialize the n x n 2D list with zeros
    spiral = [[0] * dim for _ in range(dim)]
    
    # Start at the center of the grid
    x, y = dim // 2, dim // 2
    
    # The first number in the spiral
    num = 1
    spiral[x][y] = num
    
    # Movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0  # Start with moving right
    
    step = 1  # Step size starts at 1
    while num < dim * dim:
        for _ in range(2):  # Two times for each step size (right/down and left/up)
            for _ in range(step):
                x += directions[dir_idx][0]
                y += directions[dir_idx][1]
                num += 1
                if 0 <= x < dim and 0 <= y < dim:  # Ensure we stay within bounds
                    spiral[x][y] = num
                else:
                    return spiral  # Exit if we are out of bounds
            # Switch direction
            dir_idx = (dir_idx + 1) % 4
        
        # Increase step size after completing a full cycle (right + down + left + up)
        step += 1
    
    return spiral
  



def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    
    # ADD YOUR CODE HERE  
    n = len(grid)
    # Find position of the number in the spiral
    for i in range(n):
        for j in range(n):
            if grid[i][j] == val:
                x, y, = i, j
                break
    # Directions to check for adjacent cells (8 directions)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), # Up, Down, Left, Right
                  (-1, -1,), (-1, 1), (1, -1), (1, 1)] # Diagonals
    
    adjacent_sum = 0
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n:
            adjacent_sum += grid[nx][ny]
    
    return adjacent_sum 





def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
