#Q1
x = int(input("Enter an integer:")) #integer
y = int(input("Enter an integer:")) #integer
z = float(input("Enter a float:")) #float

print("You have entered: "+str(x)+", "+str(y)+", and "+str(z))

w = x + y + z
v = x * y * z

print("The sum is:",w, "and", "the product is:", v)

#Q2 

y=int(input("Enter an integer between 12 and 20:")) #integer
if 12 <= y <= 20:
    x = print("The number in decimal is:", y)
    print("The number in binary is:", bin(y))
    print("The number in hex is:", hex(y))
else:
    print('Invalid')
    
     

#Q3
    
z=int(input("Enter an integer between 3 and 6:")) #integer
count=1
total=0
while (count <= z):
    total = total + count**3
    count += 1
    
print("sum of cubes for", z , "=", total)


#Q4

x = "Your number is"
n = int(input("Enter an integer n (positive, negative or zero):")) #integer
if n > 0:
      print(x,"a positive integer")
      
elif n == 0:
    print(x, "0")

elif n < 0:
    print(x, "a negative integer")


#Q5


n = int(input("Enter an integer n:"))

if (n % 2 != 0): # remainder is not equal to 0
    print("Your number is an odd number")

elif (n % 2 == 0): # remainder is equal to 0
    print("Your number is an even number")
       

#Q6

y = int(input("Enter an integer score (0-100):"))

x = "Your numeric grade is"
w = "\nYour letter grade is"

if (y >= 93):
    print(x, w, "A")

elif (84 <= y <= 92):
    print(x, y, w, "B")
    
elif (75 <= y <= 83):
    print(x, y, w, "C")
    
elif (60 <= y <= 74):
    print(x, y, w, "D")
    
elif (y < 60):
    print(x, y, w, "F")


#Q7

# tmp = float(19 // 5)
# val = tmp * 3 % 5

# tmp == 3.0
# val == 4.0


#Q8

# Before running the program (Manually), the program on the left side of the table would print:
# too hot

# While the program on the right side of the table would print:
# too hot
# just right

#Results after running the program were the same as previously. My reasoning is:
# Since elif is a function that allows only one fulfilled check. If the first condition is satisfied, it does not check the others conditions, and it prints out the string of the first condition.
# While with functions if*3, IDLE goes through each condition to see if they are satisfied and print out every condition fulfilled












