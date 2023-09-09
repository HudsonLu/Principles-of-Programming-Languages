w,x,y=10,2,8
try:
    print(w / x)       # Prints 5.0
    print(y / (x - 1)) # Exception!
    print(x / y)       # Skipped.
except Exception as e:
    print('Exception:', e)
else:
    print('OK')    # Never reached.
print('Done')      # Final message.
