import sys

print(sys.argv)

for argument in sys.argv[1:]:
    x = int(argument)
    if x < 0:
        print("Value can't be negative.",
              file = sys.stderr)
        sys.exit(-1) # Exit code
    else:
        print(x ** 0.5) # Square root


