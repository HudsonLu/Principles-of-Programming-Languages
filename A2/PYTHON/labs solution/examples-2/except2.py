while True:
    try:
        x = input('OK? ')
        n = int(x) # Can raise ValueError
        print(10 / n) # Can divide by zero
    except ValueError as exc:
        print('Value Error',exc)
    except ZeroDivisionError as exc:
        print('ZeroDivisionError',exc)
    except Exception as exc:
        print('Exception',exc)
    else:
        print('OK!')
