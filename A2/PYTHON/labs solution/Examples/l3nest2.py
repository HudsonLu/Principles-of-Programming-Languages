# Compute 'triangular' numbers.
msg = 'Enter a number or q to quit: '
string = input(msg)
while string != 'q':
   number = int(string)
   total = 0
   counter = 1
   while counter <= number:
       total += counter
       counter += 1
   print("The total of numbers 1 to",
         number, "is", total)
   string = input(msg)
print("Finished.")
