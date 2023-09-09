#Factorial = n x (n-1) x (n-2) x ... 1
x = int(input("Enter an integer: "))
y = 1
n = x
while n > 0:
    y *= n   # y = y * n first looping statement
    print ("y=",y)
    n -= 1   # n = n - 1 second looping statement
    print("n=",n)
# This statement follows the loop!
print(x, 'factorial is', y)
