def main():
    plate: str = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    chars = list(s)
    if len(chars) < 2 or len(chars) > 6:
        return False
    if not chars[0].isalpha() and not chars[1].isalpha():
        return False
    for index in range(len(chars)):
        if chars[index] in ",. ":
            return False
        if chars[index].isdecimal():
            if chars[index] == "0" and chars[index - 1].isalpha():
                return False
            for char in chars[index:]:
                if char.isalpha():
                    return False
    return True


if __name__ == "__main__":
    main()
