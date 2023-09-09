def sum_r(lst):
    '''Recursive sum of a list.'''
    if len(lst) != 0:
        return lst[0] + sum_r(lst[1:])
    else:
        return 0

print(sum_r([10, 5]))          # 15
print(sum_r([1, 5, 9, 6, 11])) # 32
print(sum_r([]))               # 0
