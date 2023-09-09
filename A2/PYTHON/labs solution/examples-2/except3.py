while True:
    try:
        x = input('OK? ')
        n = int(x) # Can raise ValueError
        print(10 / n) # Can divide by zero
    except (ValueError,
            ZeroDivisionError) as exc:
        print('Ex1',exc)
    else:
        print('OK!')
