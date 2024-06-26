# Fuel.py

def main():
    while True:
        fraction = input("Enter the fuel level (X/Y): ").strip()
        try:
            percentage = convert_to_percentage(fraction)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert_to_percentage(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError("The denominator cannot be zero.")
    if x > y:
        raise ValueError("The numerator cannot be greater than the denominator.")
    
    percentage = (x / y) * 100
    return round(percentage)

if __name__ == "__main__":
    main()