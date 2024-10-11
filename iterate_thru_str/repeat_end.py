while True:
    phrase = input()
    repetitions = int(input())

    phrase = phrase[len(phrase)-repetitions:]

    for a in range(repetitions):
        print(phrase,end="")

    print("\n")