def factorial(x):
    '''Compute the factorial of 'x'.'''
    r, n = 1, 1
    while n <= x:
        r *= n
        n += 1
    return r

# Choosing different names here
# leaves us with the exact same
# program, functionally!!
x = int(input('Enter a number: '))
y = factorial(x)
print('The factorial of', x, 'is', y)


    
