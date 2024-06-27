def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            number_started = True
            if char == '0' and i == len(s) - 1:
                return False
            if s[i:].isdigit():
                break
            else:
                return False
        elif number_started:
            return False

    return True

if __name__ == "__main__":
    main()