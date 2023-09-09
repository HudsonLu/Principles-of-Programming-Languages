def fib(n):
    if n <= 1:
        return n
    else:
        # 2 recursive calls.
        return fib(n - 1) + fib(n - 2)

for i in range(10):
    print(fib(i), end=' ')
print()


