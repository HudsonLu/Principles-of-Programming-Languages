matrix = [ [1, 3, 8], [6, 5, 4],
           [7, 2, 9] ]
total = 0
for row in matrix:
    print("row=",row)
    for val in row:
        print("val=",val)
        total += val
print(total) # Prints 45
