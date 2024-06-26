pip install inflect

import sys
import inflect

def main():
    # Initialize the inflect engine
    p = inflect.engine()
    
    names = []
    
    # Prompt the user for names until EOF is encountered
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print()
            break

    # Generate the farewell message
    if names:
        farewell_message = "Adieu, adieu, to " + p.join(names)
        print(farewell_message)

if __name__ == "__main__":
    main()