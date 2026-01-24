import sys

def main():
    plate = input("Plate: ")

    # If invalid, exit with code 1
    if not is_valid(plate):
        sys.exit(1)

    # Only valid plates print "Valid"
    print("Valid")


def is_valid(s):
    """Return True if s meets all vanity plate rules, False otherwise."""

    # Rule 1: length 2–6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: first two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Track if number has started
    number_started = False

    for char in s:
        if char.isdigit():
            # Rule 5: first number cannot be 0
            if not number_started and char == "0":
                return False
            number_started = True
        else:
            # Letters cannot appear after a number
            if number_started:
                return False
            # Only letters and numbers allowed
            if not char.isalpha():
                return False

    return True


if __name__ == "__main__":
    main()



