import sys


def main():
    if len(sys.argv) > 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        result = lines(sys.argv[1])
        print(result)
    except FileNotFoundError:
        sys.exit("File does not exist")


def lines(arg):
    count = 0
    with open(arg) as file:
        for line in file:
            line = line.lstrip()
            if line == "" or line.startswith("#"):
                continue
            else:
                count += 1
    return count


if __name__ == "__main__":
    main()
