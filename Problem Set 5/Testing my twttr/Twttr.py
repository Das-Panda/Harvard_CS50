def main():
    # Prompt the user for input and print the shortened version
    user_input = input("Enter a string: ")
    print(shorten(user_input))

def shorten(word):
    # Define the vowels to remove
    vowels = "aeiouAEIOU"
    # Return a new string with all vowels removed
    return ''.join(char for char in word if char not in vowels)

if __name__ == "__main__":
    main()