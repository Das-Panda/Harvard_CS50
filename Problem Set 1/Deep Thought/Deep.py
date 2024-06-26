# deep.py

def main():
    # Prompt the user for the answer to the Great Question of Life, the Universe and Everything
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

    # Check if the answer is correct
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

# Call the main function
if __name__ == "__main__":
    main()