# faces.py

def convert(text):
    """
    This function takes a string as input and converts any :) to 🙂 and :( to 🙁.
    """
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    # Prompt the user for input
    user_input = input("Please enter some text: ")

    # Convert the input using the convert function
    converted_text = convert(user_input)

    # Print the converted text
    print(converted_text)

# Call the main function
if __name__ == "__main__":
    main()