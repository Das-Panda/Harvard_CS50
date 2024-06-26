# Outdated.py

def main():
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()
        try:
            # Try to parse date in MM/DD/YYYY format
            month, day, year = parse_slash_date(date)
            break
        except ValueError:
            try:
                # Try to parse date in 'Month Day, Year' format
                month, day, year = parse_written_date(date, months)
                break
            except ValueError:
                pass
    
    # Format and print the date in YYYY-MM-DD format
    print(f"{year}-{month:02}-{day:02}")

def parse_slash_date(date):
    month, day, year = date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError
    return month, day, year

def parse_written_date(date, months):
    parts = date.split()
    if len(parts) != 3:
        raise ValueError
    month_str, day_str, year_str = parts
    month = months.index(month_str) + 1
    day = int(day_str.rstrip(","))
    year = int(year_str)
    if day < 1 or day > 31:
        raise ValueError
    return month, day, year

if __name__ == "__main__":
    main()