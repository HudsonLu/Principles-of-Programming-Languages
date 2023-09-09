def factorial(x):
    if x < 0:
        print("Negative input.")
        return None # Signal an error
    r, n = 1, 1
    while n <= x:
        r *= n
        n += 1
    return r        # Return actual result.
