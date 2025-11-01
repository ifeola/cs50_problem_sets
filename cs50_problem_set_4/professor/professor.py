import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for index in range(3):
            try:
                answer = x + y
                result = int(input(f"{x} + {y} = "))
                if not result == answer:
                    print("EEE")
                else:
                    score += 1
                    break
            except ValueError:
                pass

        if index == 2:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
