#Hudson Xingcheng Lu              2031140

#420-LCU Computer Programming, Section #00002
# S. Hilal, instructor
# Lab 9

#1 Basics


#1

colors = {'red':10, 'blue':20, 'green':30 }
print(colors) #{'red': 10, 'blue': 20, 'green': 30}

# Yes, it is the same order as I've typed. It remembers the order which I entered the items. However, it cannot sort. Compared to list, dictionaries are unordered
# Elements(items) in dictionaries can be accessed by keys/values and not by position so their position in the order of elements does not matter.




#2

colors['yellow'] = 40
colors['orange'] = 50
print(colors) #{'red': 10, 'blue': 20, 'green': 30, 'yellow': 40, 'orange': 50}

#3

for key in colors:
    print(key)
    
#red
#blue
#green
#yellow
#orange

#4

for key in colors:
    print(key, colors[key]) # index dictionary by key

#red 10
#blue 20
#green 30
#yellow 40
#orange 50


for key, val in colors.items(): #another option
    print(key, val)

#blue 20
#green 30
#yellow 40
#orange 50

for val in colors.values():
    print(val)

#10
#20
#30
#40
#50

    
#5

print(sum(colors.values()))

#6
colors['yellow'] += 1
colors['green']+= 1
colors['blue']+= 1
colors['orange']+= 1
colors['red']+= 1
print(colors)

#7

for key in sorted(colors):
    print(key)

#blue
#green
#orange
#red
#yellow


    
#8
#,print(colors['pink'])
#KeyError: 'pink'
# When reading a nonexistent item, it will raise an exception


#9

print(colors.get('red')) # 11
# since red is already in the dict, it shows the value of d, the default value.
print(colors.get('pink')) # None
# since pink is not in the dict and no value is provided, it raises None.


#10

print(colors.get('red', -1)) # 11
print(colors.get('pink', -1)) # -1
# if the key exists in the dictionary, it returns the acutal key value.
# if the key is not there, create with value =-1

#11

x = dict() #An empty dict is False.
y = x
z = x.copy()
print(x is y, x is z) # True False
print(x == y, x == z) # True True
# y is an alias for x (same object in memory)
# z is an actual copy of x (different object in memory)

# The difference between is and == is that
# The == operator compares the value of two objects,
# While, the is operator checks if two variables point to the same object in memory. 

z[2.0] = 'two'
y[3.14159] = 'pi'
y[2.71828] = 'e'
print(x, z) #{3.14159: 'pi', 2.71828: 'e'} {2.0: 'two'}, add values
y.clear()
print(x, z) #{} {2.0: 'two'}

#since we add 2.0:'two'  to z, which a copy, it does not disappear when we clear y
# while y is an alias for x, so they are connected to the same object memory. Whne we clear y, is clear x as well.

#12


from string import ascii_lowercase
letters = dict.fromkeys(ascii_lowercase , 0)
print(letters)

#{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
#'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

#13

k = [2001, 2006, 2011, 2016] #years of censuses
v = [1039534, 1620693, 1649519, 1704694] #population
d = dict(zip(k, v))
print(d) # {2001: 1039534, 2006: 1620693, 2011: 1649519, 2016: 1704694}

#14

inv_d = dict(zip(d.values(), d.keys()))
print (inv_d)
#{1039534: 2001, 1620693: 2006, 1649519: 2011, 1704694: 2016}


#2 Application 1 - Letter frequencies



from string import ascii_uppercase, ascii_lowercase


def LetterFrequencies(fx):
    y = dict.fromkeys(ascii_uppercase, 0)
    x_1 = dict.fromkeys(ascii_lowercase, 0)


    for letter in fx:
        if letter.isalpha():
            if letter.isupper():
                if letter in y:
                    y[letter] +=1
                else:
                    y[letter] = 0

            if letter.islower():
                if letter in x_1:
                    x_1[letter] +=1
                else:
                    x_1[letter] = 0
        x_1.update(y)
    return x_1

x = open("alice.txt") # x= open("/Users/hudson/Documents/Lab_9/alice.txt")  
fx = x.read()
dx=LetterFrequencies(fx)
print(dx)
x.close()










