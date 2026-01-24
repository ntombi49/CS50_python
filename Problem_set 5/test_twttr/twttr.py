
def main():
    text= input("Enter a text: ")
    print(shorten(text))

def shorten(text):
    vowels= ["a", "e", "i", "o", "u"]
    newtext= ""
    for char in text:
        if char.lower() not in vowels:
            newtext += char
    return(newtext)


if __name__ == "__main__":
    main()
