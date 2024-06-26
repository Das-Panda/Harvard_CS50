# Meal.py

def main():
    # Prompt the user for a time
    time = input("Enter the time (in 24-hour format, e.g., 7:30 or 12:45): ").strip()

    # Convert the input time to hours as a float
    hours = convert(time)

    # Determine the meal time and output the result
    if 7 <= hours <= 8:
        print("It's breakfast time.")
    elif 12 <= hours <= 13:
        print("It's lunch time.")
    elif 18 <= hours <= 19:
        print("It's dinner time.")

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = time.split(":")
    
    # Convert hours and minutes to float
    hours = float(hours)
    minutes = float(minutes)
    
    # Convert the time to hours as a float
    return hours + (minutes / 60)

if __name__ == "__main__":
    main()