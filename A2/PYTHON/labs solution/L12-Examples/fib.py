def fib(n):
    f0,f1=0,1
    while n > 0:
        f0,f1=f1,f0+f1
        n -= 1
    return f0

# If run as a script, run this.
if __name__ == "__main__":
    for i in range(10):
        print(fib(i), end=' ')
    print()
