def main():
    word = input("Input: ")
    result = shorten(word)
    print(f"Output: {result}")


def shorten(word):
    sentence = ""
    for letter in word:
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            sentence += letter
    return sentence


if __name__ == "__main__":
    main()
