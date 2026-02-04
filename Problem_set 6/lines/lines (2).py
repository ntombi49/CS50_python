import sys

def main():
    # Check for exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit(1)

    filename = sys.argv[1]

    # Check file extension
    if not filename.endswith(".py"):
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                stripped = line.strip()
                if stripped == "":
                    continue
                if stripped.startswith("#"):
                    continue
                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit(1)


if __name__ == "__main__":
    main()

