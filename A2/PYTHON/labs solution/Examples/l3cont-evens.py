# Print even numbers from 1 to n
n=int(input("Enter a positive int>0:"))
number = 0
while (number <= n):
    number = number + 1
    if (number % 2) != 0:
        continue
    print(number)
    
