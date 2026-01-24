def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    # Convert greeting to lowercase to make it case-insensitive
    greeting_lower = greeting.lower()

    if greeting_lower.startswith("hello"):
        return 0
    elif greeting_lower.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
