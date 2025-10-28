def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:1].isalpha():
        return False
    if s[0:1].isalpha() and s[-1].isalpha():
        return False
    for char in s:
        if char in ",. ":
            return False
        if char == "0" and char
    return True


if __name__ == "__main__":
    main()
