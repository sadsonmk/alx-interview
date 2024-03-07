#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a matrix (list of lists) of integers representing
      the Pascal’s triangle of size n

    Args:
        n: an integer representing the size of the Pascal's triangle

    Returns:
        A matrix (list of lists) of integers representing
        the Pascal’s triangle of size n
    """
    if n <= 0:
        return []

    matrix = [[] for i in range(n)]

    # use for loops to loop through the matrix
    for row in range(n):
        # the column is terminating at row + 1
        for col in range(row + 1):

            if col == 0 or row == col:
                matrix[row][col] = 1
            # property 4
            else:
                matrix[row][col] = \
                    matrix[row - 1][col] + matrix[row - 1][col - 1]
    return matrix
