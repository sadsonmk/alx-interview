def pascal_triangle(n):
    """Returns a matrix (list of lists) of integers representing the Pascal’s triangle of size n
    
    Args:
        n: an integer representing the size of the Pascal's triangle
    
    Returns:
        A matrix (list of lists) of integers representing the Pascal’s triangle of size n
    """
    if n <= 0: # if n is less than or equal to 0, return an empty list
        return []
    matrix = [[1]] # initialize the matrix with the first row
    for i in range(1, n): # iterate through the rows of the matrix
        row = [1]   # initialize the row with the first element
        for j in range(1, i):   # iterate through the elements of the row
            row.append(matrix[i - 1][j - 1] + matrix[i - 1][j])  # append the sum of the two elements above the current element
        row.append(1)   # append the last element of the row
        matrix.append(row) # append the row to the matrix
    return matrix   # return the matrix
print(pascal_triangle(5))
