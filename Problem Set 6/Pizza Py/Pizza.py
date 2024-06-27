pip install tabulate

import sys
import os
import csv
from tabulate import tabulate

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python Pizza.py <filename>")
    
    filename = sys.argv[1]
    
    # Check if the file has a .csv extension
    if not filename.endswith(".csv"):
        sys.exit("Error: The file must have a .csv extension")
    
    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit("Error: The specified file does not exist")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = list(reader)
            # Print the table using tabulate with grid format
            print(tabulate(data[1:], headers=data[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("Error: The specified file does not exist")

if __name__ == "__main__":
    main()