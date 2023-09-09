def factorial(x):
   r, n = 1, 1
   while n <= x:
     r *= n
     n += 1
   return r

print(factorial(10))
print(factorial(6))
print(factorial(0))
print(factorial(1))
