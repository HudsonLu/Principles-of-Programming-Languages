fp = open('test.txt', "w")
n = fp.write("First line") # Need '\n'
m = fp.write("Second line")
print(n, m)        # Prints 11 12 
print(fp.tell())   # Prints 23
fp.close()

