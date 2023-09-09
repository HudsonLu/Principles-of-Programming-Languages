fp = open('students.txt')
"""
while True: # keep reading
    line = fp.readline()
    if not line: break
    line=line.strip('\n') # remove EOLine
    # Insert code to process and store record here
    record = line.split(",")
    print(record)
"""
for line in fp.readlines():
    line=line.strip('\n')
    record=line.split(",")
    print(record)
fp.close()
"""
for line in fp:
    line=line.strip('\n')
    record=line.split(",")
    print(record)
fp.close()
"""
