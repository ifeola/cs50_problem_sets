from emoji import emojize


def main():
    text = input("Input: ")
    result = get_emoji(text)
    print(f"Output: {result}")


def get_emoji(text):
    return emojize(text, language="alias")


if __name__ == "__main__":
    main()
