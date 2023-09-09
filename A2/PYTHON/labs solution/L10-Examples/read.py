fp = open('alice.txt', 'r')
txt1 = fp.read(100) # First 100 bytes
print(len(txt1)) # Print 100
txt2 = fp.read(500) # Rest of file.
print(len(txt2)) # Print 148440
fp.close()

