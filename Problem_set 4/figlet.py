import sys
import pyfiglet
import random

def main():
    figlet = pyfiglet.Figlet()
    fonts = figlet.getFonts()

    # Case 1: No command-line arguments is random font
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))

    # Case 2: Two command-line arguments
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        figlet.setFont(font=sys.argv[2])

    # Any other number of arguments gives an error
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
