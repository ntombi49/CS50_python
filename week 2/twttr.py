text = input("Input: ")

vowels = "aeiouAEIOU"

for char in text:
    if char not in vowels:
        print(char, end="")

print()
