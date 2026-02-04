import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    valid_exts = (".jpg", ".jpeg", ".png")

    input_ext = input_path.lower().rsplit(".", 1)[-1]
    output_ext = output_path.lower().rsplit(".", 1)[-1]

    if f".{input_ext}" not in valid_exts or f".{output_ext}" not in valid_exts:
        sys.exit("Invalid file extension")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input file does not exist")

    shirt = Image.open("shirt.png")

    resized = ImageOps.fit(input_image, shirt.size)

    resized.paste(shirt, shirt)
    resized.save(output_path)


if __name__ == "__main__":
    main()
