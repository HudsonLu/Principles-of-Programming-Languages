string = input("Enter a string: ")    
result = ''
for c in string:
  if c.lower() in 'aeiou':
    continue   # ignore vowels
  result += c
print(result)
