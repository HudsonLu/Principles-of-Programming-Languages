def my_index(my_list, value):
    for ind in range(len(my_list)):
        if value == my_list[ind]:
            return ind
    raise ValueError('Value ' + str(value) +
                     ' not found.')

L= [1,2,3]
x=my_index(L,4)
y=x+5
