# plates.py

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length of the plate is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check if the plate starts with at least two letters
    if not s[0:2].isalpha():
        return False

    # Check for invalid characters and ensure numbers are at the end
    if not check_characters_and_position(s):
        return False

    return True

def check_characters_and_position(s):
    # Flags to check if we are in the numeric part of the plate
    seen_number = False

    for i, c in enumerate(s):
        if c.isdigit():
            if c == '0' and not seen_number:
                return False  # First number cannot be '0'
            seen_number = True
        elif not c.isalpha():
            return False  # No periods, spaces, or punctuation marks allowed
        elif seen_number:
            return False  # No letters allowed after numbers start

    return True

if __name__ == "__main__":
    main()