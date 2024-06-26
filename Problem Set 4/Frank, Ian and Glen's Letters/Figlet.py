pip install pyfiglet

import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # If no command-line arguments, use a random font
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    # If two command-line arguments
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        # Check if the specified font is available
        if font not in figlet.getFonts():
            sys.exit("Error: Specified font not found.")
    else:
        sys.exit("Usage: python Figlet.py [-f FONT]")

    # Set the font
    figlet.setFont(font=font)

    # Prompt the user for a string of text
    text = input("Enter text: ")

    # Output the text in the desired font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()