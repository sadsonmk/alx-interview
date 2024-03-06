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
    matrix = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        row.append(1)
        matrix.append(row)
    return matrix
