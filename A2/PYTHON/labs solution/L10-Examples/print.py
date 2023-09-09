fp = open('log.txt', 'w')
x, y = 5, 2
z = x + y
print(x, y, file = fp) # Write 5 2 on a line.
print(z, file = fp) # Write 7 on one line.
print("The end!", file = fp) # Final line.
fp.close()
