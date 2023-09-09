def rev_r(lst):
    if len(lst) > 0:
        return rev_r(lst[1:]) + lst[:1]
    return []

x = [9, 7, 4, 1, 5]
print(rev_r(x)) # [5, 1, 4, 7, 9]
