"""Hudson Xingcheng Lu              2031140
420-LCU Computer Programming, Section # 
S. Hilal, instructor 
Lab 12



(Incomplete)
"""

import math



class vector(object):
    '''A class that represents a simple vector in 0 or more dimensions.'''
    def __init__(self, comp=[]):
        self.components = comp
        self.size = len(comp)

    def __repr__(self):
        vector_info = "vector("
        if len(self.components) > 0:
            vector_info += str(self.components) #create a string from list
        return (vector_info + ')'), self.size, 

    
    def __eq__(self, other):
        return self.components == other.components and self .size == other.size


    def magnitude(self):
        mag += components**2
        return math.sqrt(mag)

    def zero(self):
        for i in self.components:   
            if (self.components[i] == 0):
                return True
            else:
                return False


    def __add__(self,other):
        #result  = []
        #result =  b.copy()
        #range
        #add elements by elements
        #result[i]
        v_new=[]
        if len(self)> len(other):
            for i in range(len(self)):
                v_new.append(self[i]+other[i])
            return vector(v_new)
        else:
            for i in range(len(other)):
                v_new.append(other[i]+self[i])
            return vector(v_new)

########### main code
"""
1. Write code to create a vector: v0 with no components. Watch for default parameter. Write code to print v0.
2. Write code to create 3 vectors: v1 with components 3,5. v2 with components 1,2,0. v3 with components 2,4,5,6.
3. Write code to print v0, v1, v2 and v3.
4. write code to print the magnitude for v3.
5. Using the class method in 1 above, write the code to check if v1 and v2 are equal.
6. Write code to check if v2 and v3 have the same magnitude.
7. Write code to check if v2 has any zero components.
8. Write code to add the 2 vectors v2 and v3.
"""
v0 = vector([])

print (v0)

v1 = vector([3,5])
v2 = vector([1,2,0])
v3 = vector([2,4,5,6])

print (v0,v1,v2,v3)

print(vector[v3].magnitude)

print(v1==v2)

print(vector[v3].magnitude==vector[v2].magnitude)

print(vector[v2].zero)

print(vector[v3].add(v2))





















        
