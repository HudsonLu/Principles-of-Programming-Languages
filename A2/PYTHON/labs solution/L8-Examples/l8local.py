def factorial(x):
    '''Compute the factorial of 'x'.'''
    r, n = 1, 1
    while n <= x:
        r *= n
        n += 1
    return r

# The 'r' and 'n' below have no
# automatic relationship to those
# used in the function!!!
r = int(input('Enter a number: '))
n = factorial(r)
print('The factorial of', r, 'is', n)


    
