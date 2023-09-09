def get_input(prompt):
    n = -1
    while True:
        x = input(prompt)
        # Beginning of try: statement.
        try:
            n = int(x)
            r = 1 / n
        except ValueError as ex:
            print('Please enter a valid integer.')
        except ZeroDivisionError as ex:
            print("Please don't enter zero.")
        else:
            print('You entered', r)
            return r
        finally:
            print('All done.')

for i in range(4):
    c = get_input('Integer ' + str(i + 1) + ': ')
    print('Result', c)
    

    
