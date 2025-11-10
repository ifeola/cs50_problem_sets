from PIL import Image, ImageOps
import sys


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        extension1 = sys.argv[1].split(".")
        extension2 = sys.argv[2].split(".")
        if not extension2[1] in ["jpg", "png", "jpeg"]:
            sys.exit("Invalid output")
        if not extension1[1] == extension2[1]:
            sys.exit("Input and output have different extensions")
        overlay(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


def overlay(arg1, arg2):
    image = Image.open(arg1)
    shirt = Image.open("./shirt.png")
    resized = ImageOps.fit(
        image,
        size=(600, 600),
        method=Image.Resampling.BICUBIC,
        bleed=0.0,
        centering=(0.5, 0.5),
    )
    resized.paste(shirt, shirt)
    resized.save(arg2)


if __name__ == "__main__":
    main()
