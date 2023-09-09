fp = open('log.txt', 'a') # Append
n = fp.tell()
print('Message starting at ', n, file = fp)
fp.close()
