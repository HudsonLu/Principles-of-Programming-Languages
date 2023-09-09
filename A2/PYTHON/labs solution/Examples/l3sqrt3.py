#
# Newton-Raphson, uses a superior method for
# generating guesses.
#
x = float(input('Enter a number: '))
y = x / 2
error = 1e-5
n_guesses = 0
while abs(y * y - x) > error:
    n_guesses += 1
    y = y - (((y * y) - x) / (2 * y))
print('Found', y, 'in', n_guesses, 'guesses')

