def my_index(my_list, value):
    for ind in range(len(my_list)):
        if value == my_list[ind]:
            return ind
    return -1 # special value if not found

x = [1, 3, 9, 8, 5, 1, 0]
n = my_index(x, 5)
if n >= 0:     # did this work?
    m = my_index(x, 2)
    if m >= 0: # did this work?
        print("Found both 5 and 2")
    else:
        print("Failed to find 2")
else:
    print("Failed to find 5")
