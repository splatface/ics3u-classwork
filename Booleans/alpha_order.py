# note all uppercases come before all lowercases
word_1 = "kitkat"
word_2 = "zoologist"
word_3 = "kazakhstan"
word_4 = "laughter"
word_5 = "meh"
word_6 = "tea"
word_7 = "subsidiary"

# all True (first comes before second)
print(f"{word_1} comes before {word_2}: {word_1 < word_2}")
print(f"{word_3} comes before {word_2}: {word_3 < word_2}")
print(f"{word_3} comes before {word_1}: {word_3 < word_1}")
print(f"{word_5} comes before {word_6}: {word_5 < word_6}")
print(f"{word_7} comes before {word_6}: {word_7 < word_6}")

print("*****")

# all False (first comes after second)
print(f"{word_4} comes before {word_1}: {word_4 < word_1}")
print(f"{word_2} comes before {word_5}: {word_2 < word_5}")
print(f"{word_6} comes before {word_3}: {word_6 < word_3}")
print(f"{word_7} comes before {word_1}: {word_7 < word_1}")
print(f"{word_2} comes before {word_4}: {word_2 < word_4}")