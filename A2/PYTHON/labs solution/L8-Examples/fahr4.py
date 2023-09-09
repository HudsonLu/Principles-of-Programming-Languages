# Convert Celsius to Fahrenheit
def c_to_f(deg_c):
    deg_f = deg_c * 9 // 5 + 32
    return deg_f

# Fahrenheit-Celsius table for c=-40,-30, ..., 100 
print("F\tC")
celsius = -40
while celsius <= 100:
    fahr = c_to_f(celsius)
    print("{}\t{}".format(fahr, celsius))
    celsius += 10
                                                                      #xxxxx
