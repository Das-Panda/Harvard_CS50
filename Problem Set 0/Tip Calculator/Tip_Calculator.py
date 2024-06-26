def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    """
    This function accepts a str as input (formatted as $##.##),
    removes the leading $, and returns the amount as a float.
    """
    # Remove the leading $ and convert to float
    return float(d.replace('$', ''))

def percent_to_float(p):
    """
    This function accepts a str as input (formatted as ##%),
    removes the trailing %, and returns the percentage as a float.
    """
    # Remove the trailing % and convert to float, then divide by 100 to get the percentage
    return float(p.replace('%', '')) / 100

main()