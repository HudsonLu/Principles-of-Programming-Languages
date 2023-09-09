strings = ["ABC", "BCC", "CAR", "DOOR", "EAR", "FOX"]
letter_count = 0
for word in strings:
    print(word)
    print(word.lower())
    letter_count += len(word)
print("Last word is", word, "with",
      letter_count, "letters.")
