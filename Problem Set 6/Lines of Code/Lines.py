import sys
import os

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python Lines.py <filename>")
    
    filename = sys.argv[1]
    
    # Check if the file has a .py extension
    if not filename.endswith(".py"):
        sys.exit("Error: The file must have a .py extension")
    
    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit("Error: The specified file does not exist")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("Error: The specified file does not exist")
    
    loc = count_lines_of_code(lines)
    print(f"Lines of code: {loc}")

def count_lines_of_code(lines):
    loc = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            loc += 1
    return loc

if __name__ == "__main__":
    main()