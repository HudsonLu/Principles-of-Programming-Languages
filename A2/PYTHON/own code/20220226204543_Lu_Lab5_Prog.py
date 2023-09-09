#Hudson Xingcheng Lu                2031140
#420-LCU Computer Programming
#S. Hilal , instructor

#Lab 5

#Part 1 - List Basics

ls1 = [2,4,8,16,32,64]
ls2 = [6,1,27,21,24,7]

if ls1 > ls2:
    print ('ls1 is greater than ls2')
else:
    print ('ls2 is greater than ls1')
    
# It analyzes the first position(integer) which is [0] in the list. Since 6<2, ls2 is greater than ls1.

ls1[-1] -= 2

print("ls1 =", ls1 )

ls3 = ls1 + ls2
print("ls3 =", ls3 )

ls1.append(12)
print("ls1 =", ls1 )
print("ls3 =", ls3 )

#ls3 do not change. It does not include the integer added with append[]

ls4 = ls2
print("ls2 =", ls2 )
print("ls4 =", ls4 )

ls2.append(22)
print("ls2 =", ls2 )
print("ls4 =", ls4 )
# Since list is mutable, and ls2 = ls4, ls2 is an alias for ls4.
# By using append() to add a new integer, it saves the data for both variables.



#Part 2 - List Methods

ID = '2031140'
ID_digits = list(ID)

print ('ID=', ID)
print ('ID_digits=', ID_digits)


x = ID.count("1")
print('There are', x, "occurrences of the digit ’1’")

y = "9"+ID
new_ID = ''.join(y)
print ('new_ID=', new_ID)



#Part 3 - introducing the for loop

#1.
full_name = 'Hudson Xingcheng Lu'
for letter in full_name:
    print(letter)
    print(letter.lower())

 
# It prints each letter double. However the first occurence of each letter in the full_name is printed  as written in the variable where upper cases are not neglected.
# However, the second time a letter repeats, it is in lower cases. (eg: Hhuuddssoonn)

      
#2.
full_name = 'Hudson Xingcheng Lu'
result = 0
for letter in full_name:
    print(letter , result)
    result += 1
    print(full_name , result)

#In each new iteration, the number of iterations is represented by the variable result.
#After each interation, it prints letter in the next position of the full_name with the result distanced by a space character(each iteration +=1)
#They are 19 iterations because the full_name is composed of 19 characters.


#3     
full_name = 'Hudson Xingcheng Lu'
result = ''
for letter in full_name:
    result = letter + result
print(result)

# The output is full_name but the letters backwardly because (result = letter + result) each iteration the new letter is added to the right side.




#Part 4 - More for loops

#1
for digit in ID_digits:
     print(digit , int(digit) % 2 != 0) # replace element by digit

#Each time, it prints an integer and it prints a Boolean that the results by doing the remainder of floor division:
#if not 1 as remainder, it will return as False.

#2

result = []
for digit in ID_digits:
      result = [digit] + result
print(result)


# It prints ID_digits in the reverse way because each time a digit it added from the left.
# Also, the brackets for digits are necessary since a list (result) with another list:
# Indeed, it prints a message, which it can only concatenate str (not "list") to str.

#3
id_backward = ''.join(result)
      
print(id_backward , 'x'.join(result))

# It prints the the student_ID backward by uniting each element of the list in the variable result
# It prints as a string and backward since a new digit is added from the left
# It also prints backwardly each digit of the variable result (that has been joined in a single string wwith each time an "x" between each digits to replace the character space each time due to join().
# It prints:
# 0411302 0x4x1x1x3x0x2















