n = 1
while n < 10:
n += 1       # ERROR: Forgot indent.

n, r = 10, 1
while n > 0:
    r *= n
   n -= 1    # ERROR: Reduced indent.

x, y = 1, 1
while x < n:
    y *= x
      x += 1 # ERROR: Extra indent.
