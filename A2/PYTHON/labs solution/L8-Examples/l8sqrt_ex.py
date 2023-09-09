x = 1                           # Global x and y
y = 2
def square_root(x):             # Local x
    '''Return the square root of 'x'.

    Uses Newton's method to compute the 
    square root to a fixed precision.'''
    y = x / 2                   # Local y
    while abs(y * y - x) > 1e-10:
        y = (y + x / y) / 2
    return y

print(square_root(2))
print(square_root(3))
print(x, y)
