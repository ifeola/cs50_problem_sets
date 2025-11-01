import random


def main():
    result = game("Level: ")
    print(result)


def guess_int(random_numb):
    while True:
        try:
            guessed_integer = int(input("Guess: "))
            if guessed_integer <= 0:
                continue
            elif guessed_integer < random_numb:
                print("Too small!")
                continue
            elif guessed_integer > random_numb:
                print("Too large!")
                continue
            else:
                return "Just right!"
        except ValueError:
            continue


def game(level):
    while True:
        try:
            numb = int(input(level))
            if not numb > 0:
                continue
            else:
                random_numb = random.randint(1, numb)
                guessed = guess_int(random_numb)
                return guessed
        except ValueError:
            continue


main()
