# Hudson Xingcheng Lu              2031140

#420-LCU Computer Programming, Section #00002
# S. Hilal, instructor
# Lab 7


def my_len(iterable):
    """
    For every "u" in iterable, for every character, it adds 1 more each time it returns.

    """
    count = 0
    for u in iterable:
        count += 1
    return count
    
# Test cases for Function my_len
print(my_len([]))
print(my_len("Marianopolis College"))
print(my_len((1,5,9,2,1)))


def my_product(my_list):
    """
    For every "u" in my_list, if the u is multiplied by another value each time it returns.

    """
    count = 1
    for u in my_list:
        count *= u 
    return count


# Test cases for Function my_product
print(my_product([1, 5, 9]))
print(my_product([10, 20, 30.0]))
print(my_product([])) #prints 0


def my_count(my_list, value):
    """
    For every "i" in my_list, if the i is equal to the value, it adds 1 more each time it returns.

    """
    count = 0
    for i in my_list:
        if i == value:
            count = count + 1
    return count

# Test cases for Function my_find       
x = [1, 2, 3, 3]
print(my_count(x, 1))
print(my_count(x, 3))
print(my_count(x, 4))



def my_find(my_list, value):
    """
    Each "u" is associated with a number in the list of range of len in the my_list.
    If the value correspond to position "u" in my_list, it prints the position.

    """
    count = -1
    for u in list(range(my_len(my_list))):
        if (my_list[u] == value) and my_count(my_list, value)<2:
            count = u
        if not (my_count(my_list, value)<2) and (my_list[u] == value):
            x = my_list[:u]
            for u in list(range(my_len(x))):
                if (x[u] == value):
                    count = u     
    return count

# Test cases for Function my_find
print(my_find([1, 5, 9, 1], 0)) #returns -1
print(my_find([1, 5, 9, 1], 9)) #returns 2
print(my_find([1, 5, 9, 1], 1)) #returns 0


###################################################
def sum_cubes_r(n):
    """
    n represents the base
    Each time it returns, it applies the function with n-1
    and it adds up
    """
    if n == 1:
        return 1
    else:
        return sum_cubes_r(n - 1) + n**3

# Test cases for Function sum_cubes_r
print(sum_cubes_r(4))
print(sum_cubes_r(5))



def my_find_r(my_list , value):
    """
    Each time value is not in my_list, it adds 1 to the position until it reaches the position of value in the my_list.
    """
    if value in my_list:
        if (my_count(my_list, value)<2):
            return my_find_r(my_list[1:] , value) +1
        
        if not(my_count(my_list, value)<2):
            return my_find_r(my_list[1:] , value) -2
    else:
        return -1
 


# Test cases for Function my_find
print(my_find_r([1, 5, 9, 1], 0)) #returns -1
print(my_find_r([1, 5, 9, 1], 9)) #returns 2
print(my_find_r([1, 5, 9, 1], 1)) #returns 0






