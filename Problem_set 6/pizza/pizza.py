import sys
import csv
from tabulate import tabulate

def main():
    # Check for exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")

    filename = sys.argv[1]

    # Check file extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            table = list(reader)

    except FileNotFoundError:
        sys.exit("File does not exist")

    # First row is the header
    headers = table[0]
    rows = table[1:]

    print(tabulate(rows, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
