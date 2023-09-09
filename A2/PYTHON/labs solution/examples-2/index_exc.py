def my_index(my_list, value):
    for ind in range(len(my_list)):
        if value == my_list[ind]:
            return ind
    raise ValueError('Value ' + str(value) +
                     ' not found.')
#Handling exceptions: Program does not fail
x = [1, 3, 9, 8, 5, 1, 0]
try:
    n = my_index(x, 8)
    m = my_index(x, 2)
except ValueError as ex:
    print(ex) # prints Value 2 not found
else:
    print("Found both 8 and 2")

z=sum(x)/len(x)
print(z)
