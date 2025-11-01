import sys
import random
from pyfiglet import Figlet


def main():
    text = generate_figlet("Input: ")
    if not text == None:
        print(f"Output: {text}")


def generate_figlet(text):
    figlet = Figlet()
    fonts = figlet.getFonts()
    length = len(fonts)
    random_number = random.randint(0, length)
    if len(sys.argv) == 1:
        prompt = input(text)
        figlet.setFont(font=fonts[random_number])
        formatted_f = figlet.renderText(prompt)
        return formatted_f

    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            prompt = input(text)
            figlet.setFont(font=sys.argv[2])
            formatted_f = figlet.renderText(prompt)
            print(sys.argv[1], sys.argv[2])
            return formatted_f
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")


main()


""" if len(sys.argv) == 1:
        figlet.setFont(font=fonts[random_number])
        formatted_f = figlet.renderText(text)
    elif len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        formatted_f = figlet.renderText(text)
    return formatted_f """
