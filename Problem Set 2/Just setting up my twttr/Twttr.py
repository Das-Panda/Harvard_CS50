# Twttr.py

def main():
    # Prompt the user for a string of text
    text = input("Enter a string of text: ")

    # Remove vowels from the text
    no_vowels_text = remove_vowels(text)

    # Output the text without vowels
    print(no_vowels_text)

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for c in text:
        if c not in vowels:
            result += c
    return result

if __name__ == "__main__":
    main()