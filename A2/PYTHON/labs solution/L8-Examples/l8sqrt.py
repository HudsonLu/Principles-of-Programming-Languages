def square_root(x):             # Local x
    '''Return the square root of 'x'.

    Uses Newton's method to compute the 
    square root to a fixed precision.'''
    y = x / 2                   # Local y
    while abs(y * y - x) > 1e-10:
        y = (y + x / y) / 2
    return y
