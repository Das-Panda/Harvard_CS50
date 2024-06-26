# Emojize.py

import emoji

def main():
    # Prompt the user for a string in English
    user_input = input("Enter a string: ").strip()

    # Convert the input string to an emojized version
    emojized_str = emoji.emojize(user_input, language='alias')

    # Output the emojized string
    print(emojized_str)

if __name__ == "__main__":
    main()