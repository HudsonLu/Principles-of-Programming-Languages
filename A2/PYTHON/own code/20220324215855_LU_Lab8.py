
#Hudson Xingcheng Lu              2031140

#420-LCU Computer Programming, Section #00002
# S. Hilal, instructor
# Lab 8

#1

# a, b, e, f

['a', 2, 5.0, []]
[+1e10]
[1+1, 2*2, 4/9, ]
[[[]]]




#2

#a)
x, y = 13.0, 4
print(x // y, x / y, x % y)
#3.0 3.25 1.0


#b)
my_list = [0]
for i in range(3):
    my_list += [2 ** i]
print(my_list)
#[0, 1, 2, 4]



#c)
x, y = -1, 19
def f(x):
    y, z = 1, 1
    while y < x:
        y, z = y * 2, y
    return z
print(f(x), f(y))
#1 16

#d)
text = 'To be or not to be'
print(text.split()[::-2])
#['be', 'not', 'be']

#e)
array = [5,4,3,2,1]
s = 0
for n in array[::2]:
    s += n
print(s)
#9

#f)
a, b, c = 'False', '', 0
print(not a or not b or not c)
#True

#g)
x, y, z = [0],"0",0 # y is the digit 0
print(bool(x and y[0]) or z, z and not y or bool(x))
#True True

#i)
x, y, z = [], [0], True
print(x and y[0] or z, z and not y or bool(x))
#True False


#h)
x = [9, 1, 0]
y = x
y.clear()
print(x)
#[]


#j)
y = []
for v in range(0, 30, 5):
    y.append(v % 2 != 0)
print(all(y))
#False

#k)
L = [3,6,8,10,11]
total = 1
while L:
    total = total * L[-1]
    L.pop()
    print(total/5)

#2.2
#22.0
#176.0
#1056.0
#3168.0


#3

def check_card_number(x):
    a = (len(x) == 16)
    b = x.isdigit()    
    if ((a and b)==True):
        c = 0
        for i in x:
            c = c + int(i)
        d = ((int(c)%2) == 0)
        e = a, b, d
        if all(e)==True:
            return True
        else:
            return False
    else:
        return False


    
    

cc1 = '5191241074527994' # sum is 70
cc2 = '5191241076621233' # sum is 53
cc3 = '51912410C6621233'  


print(check_card_number(cc1)) #prints True
print(check_card_number(cc2)) #prints False
print(check_card_number(cc3)) #prints False



#4

def count_capitalized(text):
    count=0
    for i in text.split():
        if i[0].isupper():
            count=count+1
    return count


# Test cases for Function count_capitalized
str1 = "Our Home and Native Land"
print(count_capitalized(str1)) # prints 4
str2 = "On Oct 10, a wedding in British Colombia has led to 49 COVID 19 cases"
print(count_capitalized(str2)) # prints 5




















    
