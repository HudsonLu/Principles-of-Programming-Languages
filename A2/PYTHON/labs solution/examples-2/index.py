def my_index(my_list, value):
    for ind in range(len(my_list)):
        if value == my_list[ind]:
            return ind
    return -1 # special value if not found
