#!/usr/bin/python3
"""a module to solve the matrix rotation problem"""


def rotate_2d_matrix(matrix):
    """a function to rotate a matrix by 90 degreees"""

    for x in range(len(matrix)):
        for y in range(x, len(matrix)):
            matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

    for x in range(len(matrix)):
        matrix[x].reverse()
