import random

# Prompt for level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Generate random number
secret = random.randint(1, level)

# Prompt for guesses
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue

        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
