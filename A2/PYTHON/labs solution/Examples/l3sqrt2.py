# Bisection search. Divide the search area
# in half on each guess. (l3sqrt2.py)
x = float(input('Enter a number: '))
lo, hi = 0, x # double assignment!
error = 1e-5
y = (lo + hi) / 2
n_guesses = 0
while abs(y * y - x) > error:
    n_guesses += 1
    if y * y > x:
        hi = y  # lower half
    else:
        lo = y   # upper half
    y = (lo + hi) / 2
print('Found', y, 'in', n_guesses, 'guesses')
