def gcd(a, b):
    '''Compute the greatest common divisor
       of positive integers 'a' and 'b'.'''
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
