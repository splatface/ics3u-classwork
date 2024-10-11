while True:
    phrase_one = input()
    phrase_two = input()
    saved_phrase = ""

    length_one = len(phrase_one)
    length_two = len(phrase_two)

    if length_one < length_two: # phrase_one will be longer than phrase_two
        saved_phrase = phrase_two
        phrase_two = phrase_one
        phrase_one = saved_phrase

    length_one = len(phrase_one)
    length_two = len(phrase_two)

    phrase_one = phrase_one[length_one - length_two:] # slices phrase_one

    if phrase_one.lower() == phrase_two.lower():
        print("True")

    else:
        print("False")