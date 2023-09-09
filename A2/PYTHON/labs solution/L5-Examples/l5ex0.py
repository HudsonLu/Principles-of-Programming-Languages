# Process a 2-dimensional matrix.
# Version 1: while loops (l5ex0.py)
matrix = [ [1, 3, 8], [6, 5, 4],
           [7, 2, 9] ]
total = 0
row_idx = 0
while row_idx < len(matrix):
    col_idx = 0
    while col_idx < len(matrix[0]):
        total += matrix[row_idx][col_idx]
        col_idx += 1
    row_idx += 1
print(total) # Prints 45
