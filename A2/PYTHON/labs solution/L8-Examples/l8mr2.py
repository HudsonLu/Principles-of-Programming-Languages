def example(n, m):
    if n < m:
        return -1
    elif n > m:
        return 1
    else:
        return 0

print(example(1, 2)) # -1
print(example(2, 1)) # 1
print(example(2, 2)) # 0
