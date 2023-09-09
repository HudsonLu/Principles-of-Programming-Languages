# Hudson Xingcheng Lu              2031140
# 420-LCU Computer Programming, Section #00002
# S. Hilal, instructor
# Lab 13

1.

#a) True
#b) False

2.
#a) 2 20 3
#b) 0 10 3
#c) 0 9 3

3.
#a) /fedcb/
#b) True True
#c) True
#d) True False
#e) ['be', 'not', 'be']
#f) 9
#g) 13
#h) False


4.

def mean_dict(dic1,dic2):
    new_dict = {}
    for i in dic2.keys():
        new_dict[i] = dic2[i]

    for i in dic1.keys():
        if (new_dict[i] != dic1[i]):
            new_dict[i] = (new_dict[i] + dic1[i])/2
            if (new_dict[i] == 0.0):
                new_dict.pop('b')
        else:
            pass 
    return new_dict

x = {'a': 2, 'b': 1, 'c': 5}
y = {'a': 3, 'b': -1, 'c': 3, 'd': 3 }


print(mean_dict(x,y)) #{’a’: 2.5, ’c’: 4.0, ’d’: 3}


5.

def recursive_power(n,x):
    return n**x

print(recursive_power(3,4)) #prints 81


6.
def get_diagonal(m):
    dil = []
    for i in range(len(m)):
        if (len(m[-1]) == len(m)):
            dil = dil + list(str(m[i][i]))
    for z in range(len(dil)):
        dil[z] = int(dil[z])
    
    if (len(m[-1]) != len(m)):
        print('Not a square matrix')         
    return dil
    
 


mat1 = [[1, 2, 3], [5, 4, 6], [9, 7, 8]]
mat2 = [[1, 2, 3], [5, 4, 6], [9, 7, 8], [10, 12, 11]]


print(get_diagonal(mat1))

print(get_diagonal(mat2))
#[1, 4, 8]
#"Not a square matrix "


