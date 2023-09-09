text_value = "Marianopolis College"
result = ""
for letter in text_value:
    if letter.isspace():
        break
    result = letter.lower() + result
print("Result", result)
