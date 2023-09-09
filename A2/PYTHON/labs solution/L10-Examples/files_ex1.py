in_file = open('alice.txt')
nl,nc,nw = 0,0,0 # Initialize counters.
for line in in_file: #in_file.readlines()
    nl += 1          # Count lines.
    nc += len(line)  # Count characters.
    nw += len(line.split())
print(nl,nc,nw)      # Print results.
in_file.close()      # Done with file.
