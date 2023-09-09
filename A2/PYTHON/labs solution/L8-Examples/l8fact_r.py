def fact(n):
    '''Recursive factorial'''
    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(10)) # 3628800



