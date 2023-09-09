string = input('Enter a string: ')
i = 0
result = ""
n = 0
while i < len(string):
  c = string[i]
  i += 1
  if c.isdigit():
    continue        # Ignore digits
  n += 1
  result += c.upper()
print(n, result)
