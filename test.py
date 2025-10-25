from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

length = len(fonts)
rand = random.randint(0, length)

if not sys.argv[1] in fonts:
    print(sys.argv[1])
else:
    print(f"found: {sys.argv[1]}")
