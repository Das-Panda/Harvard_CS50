# Camel.py

def main():
    # Prompt the user for the name of a variable in camel case
    camel_case = input("Enter a variable name in camel case: ").strip()

    # Convert the camel case name to snake case
    snake_case = convert_to_snake_case(camel_case)

    # Output the snake case name
    print("The corresponding snake case name is:", snake_case)

def convert_to_snake_case(camel_case):
    snake_case = ""
    for c in camel_case:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    return snake_case

if __name__ == "__main__":
    main()