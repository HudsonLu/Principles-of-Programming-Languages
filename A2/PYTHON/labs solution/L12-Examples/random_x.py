>>> from random import *
>>> random()
0.6876409240484214
>>> random()
0.5700914449200836
>>> randint(1, 100) # prints 60
>>> randint(1, 100) # prints 85
>>> x = list(range(10))
>>> print(x)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> shuffle(x)
>>> print(x)
[9, 3, 7, 8, 0, 1, 2, 6, 4, 5]
>>> choice(x) # prints 4
>>> choice(x) # prints 0

