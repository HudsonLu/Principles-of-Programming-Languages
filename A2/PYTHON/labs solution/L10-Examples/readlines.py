fp = open('alice.txt')
for line in fp.readlines(): # Or just fp:
    if len(line) >= 72:
        print(line.strip())
fp.close()
