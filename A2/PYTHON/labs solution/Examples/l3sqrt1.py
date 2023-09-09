# Exhaustive enumeration - search for the
# square root by starting at zero and
# counting up.
x = float(input('Enter a number: '))
tiny = 1e-6
error = 1e-5
y = 0
n_guesses = 0
while abs(y * y - x) > error:
    n_guesses += 1         # count guesses!
    y += tiny
print('Found', y, 'in', n_guesses, 'guesses')

