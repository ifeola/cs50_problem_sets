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


""" from PIL import Image, ImageOps
import sys
from pathlib import Path


def main():
    # Validate number of arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.jpg output.jpg")

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    # Validate extensions
    valid_exts = {".jpg", ".jpeg", ".png"}
    if output_path.suffix.lower() not in valid_exts:
        sys.exit("Invalid output format")
    if input_path.suffix.lower() != output_path.suffix.lower():
        sys.exit("Input and output have different extensions")

    # Try processing
    try:
        overlay(input_path, output_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    except OSError:
        sys.exit("Error processing image file")


def overlay(input_path, output_path):
    image = Image.open(input_path)
    shirt = Image.open("shirt.png")

    # Resize image to match shirt dimensions
    resized = ImageOps.fit(
        image,
        size=shirt.size,
        method=Image.Resampling.BICUBIC
    )

    # Overlay shirt (using alpha transparency)
    resized.paste(shirt, (0, 0), shirt)

    # Save result
    resized.save(output_path)


if __name__ == "__main__":
    main() """
