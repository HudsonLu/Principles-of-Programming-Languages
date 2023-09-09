x = 3 # Input number.
y = 1 # Initial guess.
guesses=0
# Repeat while |y*y - x| > 1e-10
while abs(y*y - x)>1e-10:
    print("y is ",y)
    y = (y + x / y) / 2 # Update
    guesses = guesses + 1 # increment count
print('The square root of', x, 'is', y)
print("guesses = ",guesses)
