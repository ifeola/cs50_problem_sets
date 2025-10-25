import inflect


def main():
    print(adieu("Name: "))


def adieu(text):
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input(text)
            names.append(name)
        except EOFError:
            return f"\nAdieu, adieu, to {p.join(names)}"


main()
