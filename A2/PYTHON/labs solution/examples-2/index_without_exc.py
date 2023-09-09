def index(list, value):
    for index in range(len(list)):
        if value == list[index]:
            return index

x = [1, 3, 9, 8, 5, 1, 0]

try:
    n = index(x, 5)
    m = index(x, 2)
    average = m*5
except TypeError as ex:
    print(ex)
else:
    print("Found both 5 and 2")

