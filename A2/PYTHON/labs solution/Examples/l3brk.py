x = float(input('Enter a number: '))
y = 1 # Initial guess.
n_guesses = 0
error = 1e-19
while abs(y * y - x) > error:
  n_guesses += 1
  if n_guesses > 500: # Limit our guesses!
    break
  y = (y + x / y) / 2  # Update
print('Found', y, 'in', n_guesses, 'guesses')

