# Interpreter.py

def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., '1 + 1'): ").strip()

    # Split the input into x, y, and z
    x, y, z = expression.split(" ")

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Initialize the result variable
    result = 0.0

    # Perform the operation based on y
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z

    # Output the result as a floating-point value formatted to one decimal place
    print(f"{result:.1f}")

# Call the main function
if __name__ == "__main__":
    main()