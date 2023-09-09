strings = ["A", "B", "C", "D", "E", "F"]
letter_count = 0
for word in strings:
    print(word.lower())
    letter_count += len(word)
print("Last word is", word, "with",
      letter_count, "letters.")
