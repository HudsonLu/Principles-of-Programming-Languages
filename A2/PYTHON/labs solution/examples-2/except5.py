while True:
    try:
        x = input('OK? ')
        n = int(x) # Can raise ValueError
        print(10 / n) # Can divide by zero
    except:
        print('Ex1')
    else:
        print('OK!')
