from datetime import date, datetime
import inflect
import sys

def main():
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)
    
    minutes = calculate_age_in_minutes(birth_date)
    words = convert_number_to_words(minutes)
    print(f"{words} minutes")

def calculate_age_in_minutes(birth_date):
    today = date.today()
    age_in_days = (today - birth_date).days
    age_in_minutes = age_in_days * 24 * 60
    return round(age_in_minutes)

def convert_number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    return words.replace(",", "")

if __name__ == "__main__":
    main()