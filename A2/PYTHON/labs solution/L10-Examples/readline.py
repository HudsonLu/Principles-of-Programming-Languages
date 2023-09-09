fp = open('alice.txt')
line = fp.readline()
while line:  # Until zero length.
    if len(line) >= 72:
        print(line.strip())
    line = fp.readline()
fp.close()
