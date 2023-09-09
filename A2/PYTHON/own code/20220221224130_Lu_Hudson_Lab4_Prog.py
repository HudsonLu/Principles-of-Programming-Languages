#Hudson Xingcheng Lu                2031140
#420-LCU Computer Programming
#S. Hilal , instructor

#Lab 4



#Part 1 -string indexing

full_name = "Hudson Xingcheng Lu"
name_len = len(full_name)
print(full_name[0])
print(full_name[-1])


# A message appears "string out of range" because it is supposed to show the 19th character, which does not exist.
# Indeed, index values range from 0 to len(full_name)-1, which end on 18th since we start from 0.


#Part 2 -string slicing and operators

#1)
full_name[0:16]
first_name_index = len(full_name[0:16])
first_name = full_name[0:16]

#2
full_name[-2:]
last_name_index = len(full_name[-2:])
last_name = full_name[-2:]

#3
print("Hello, "+first_name)

#4
if full_name.lower() > 'nnn':
    print("greater")

elif full_name.lower() < 'nnn':
    print("smaller")
        
    
#5
full_name = "Hudson Xingcheng Lu"
     
"an" in full_name
if True:
    print('There is no "an" in my name')
elif False:
    print('There is "an" in my name')


#Part 3 -string methods

#1
Index = full_name.find('son')

#2
final_space = full_name.rindex(" ")

#3

x = full_name[final_space+1:]
print("The last part of my name is", x)

#4
y = full_name[:final_space]
print("The first part of my name is", y)

#5

full_name.replace('a', '-').replace('e', '-').replace('i', '-').replace('o', '-').replace('u', '-')

#6

print(full_name[0].lower()+full_name[1:].upper())

#7
header = 'From jsmith@gmail.com Wed Feb 03 9:32:39 2021\n'
x = header.index("@")
y = header.index(" ",x)

print(header[x:y])

#Part 4 - while, if, and strings

print("""

Enter a password that respect the following criteria:
1. password must be composed of letters and digits only except for last character which must be a #.
2. Minimum length 8 characters and maximum length 15 characters (inclusive).
3. Password must start with a capital letter.
4. At least 1 digit.
5. At least 1 small letter.
""")



count = 0
while (count < 9):
    n = input("Enter a password:")
    if not n.endswith("#"):
        print("Your password must be composed of letters and digits only except for last character which must be a #")
        count = 0
        continue
        

    if (8 > len(n) or len(n) > 15):
        print("Minimum length 8 characters and maximum length 15 characters (inclusive)")
        count = 0
        continue  

    if not n[0].isupper():
        print("Password must start with a capital letter")
        count = 0
        continue      
        
    if not n.find('0123456789'):
        print("At least 1 digit")
        count = 0
        continue     
        
    if not n.find('abcdefghijklmnopkrstuvwxyz'):
        print("At least 1 small letter")
        count = 0
        continue
  
    else:
        print("Password accepted")
        count = 9
  

        

        
















    
